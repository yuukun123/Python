import js
from pyodide import create_proxy
import random
from math import sin, cos, radians
from datetime import datetime, timedelta

# Sử dụng js.Math để thay thế cho một số hàm trong pygame.math
# vì pygame.math không được hỗ trợ đầy đủ trong Pyodide
from js import Math

# Màu sắc
PALETURQUOISE = (175, 238, 238)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_RED = (255, 150, 150)
RED = (255, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Khởi tạo canvas
canvas = js.document.getElementById("myCanvas")
ctx = canvas.getContext("2d")

# Kích thước canvas
WIDTH, HEIGHT = 800, 600
canvas.width = WIDTH
canvas.height = HEIGHT

# Lớp Particle (hạt pháo hoa)
class Particle:
    def __init__(self, x, y, angle, speed, color):
        self.x = x
        self.y = y
        self.vx = speed * Math.cos(radians(angle))  # Sử dụng js.Math.cos
        self.vy = speed * Math.sin(radians(angle))  # Sử dụng js.Math.sin
        self.color = color
        self.lifetime = random.randint(50, 120)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 1

    def draw(self, ctx):
        if self.lifetime > 0:
            ctx.beginPath()
            ctx.arc(self.x, self.y, 3, 0, 2 * Math.PI)  # Sử dụng js.Math.PI
            ctx.fillStyle = f"rgb({self.color[0]}, {self.color[1]}, {self.color[2]})"
            ctx.fill()

# Lớp Firework (pháo hoa)
class Firework:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 100)
        self.y = HEIGHT
        self.target_y = random.randint(100, HEIGHT // 2)
        self.color = random.choice(COLORS)
        self.particles = []
        self.exploded = False

    def update(self):
        if not self.exploded:
            self.y -= 5
            if self.y <= self.target_y:
                self.exploded = True
                self.create_particles()
        else:
            for particle in self.particles:
                particle.update()
            self.particles = [p for p in self.particles if p.lifetime > 0]

    def create_particles(self):
        for angle in range(0, 360, 12):
            speed = random.uniform(2, 5)
            self.particles.append(Particle(self.x, self.y, angle, speed, self.color))

    def draw(self, ctx):
        if not self.exploded:
            ctx.beginPath()
            ctx.arc(self.x, self.y, 5, 0, 2 * Math.PI)  # Sử dụng js.Math.PI
            ctx.fillStyle = f"rgb({self.color[0]}, {self.color[1]}, {self.color[2]})"
            ctx.fill()
        else:
            for particle in self.particles:
                particle.draw(ctx)

# Hàm hiển thị Happy New Year và pháo bông
def show_happy_new_year(current_time):
    ctx.clearRect(0, 0, WIDTH, HEIGHT)

    # Hiển thị chữ "Happy New Year!"
    ctx.font = "80px Arial"
    ctx.fillStyle = "white"
    ctx.textAlign = "center"
    ctx.fillText("Happy New Year!", WIDTH / 2, HEIGHT / 2)

    # Tạo hiệu ứng pháo hoa
    fireworks = [Firework() for _ in range(5)]
    end_time = current_time + timedelta(seconds=38)

    def animate_fireworks():
        nonlocal fireworks
        ctx.clearRect(0, 0, WIDTH, HEIGHT)
        ctx.fillStyle = "rgb(175, 238, 238)"
        ctx.fillRect(0, 0, WIDTH, HEIGHT)

        ctx.font = "80px Arial"
        ctx.fillStyle = "white"
        ctx.textAlign = "center"
        ctx.fillText("Happy New Year!", WIDTH / 2, HEIGHT / 2)

        for firework in fireworks:
            firework.update()
            firework.draw(ctx)

        # Sửa lỗi logic: chỉ loại bỏ pháo hoa khi đã nổ và hết hạt
        fireworks = [fw for fw in fireworks if (not fw.exploded) or fw.particles]
        if random.random() < 0.02:
            fireworks.append(Firework())

        if datetime.now() < end_time:
            js.requestAnimationFrame(create_proxy(animate_fireworks))

    js.requestAnimationFrame(create_proxy(animate_fireworks))

# Hàm tính thời gian còn lại đến thời điểm đích
def get_time_to_target(target_time):
    now = datetime.now()
    remaining = target_time - now
    return max(0, remaining.total_seconds())

# Hàm countdown
def countdown_to_target(target_time):
    def update_countdown():
        remaining_seconds = get_time_to_target(target_time)
        if remaining_seconds <= 0:
            show_happy_new_year(datetime.now())
            return

        hours = int(remaining_seconds // 3600)
        minutes = int((remaining_seconds % 3600) // 60)
        seconds = int(remaining_seconds % 60)

        ctx.clearRect(0, 0, WIDTH, HEIGHT)
        ctx.fillStyle = "rgb(175, 238, 238)"
        ctx.fillRect(0, 0, WIDTH, HEIGHT)

        ctx.font = "60px Arial"
        ctx.fillStyle = "white"
        ctx.textAlign = "center"
        ctx.fillText("Countdown", WIDTH / 2, HEIGHT / 4)

        ctx.font = "80px Arial"
        ctx.fillStyle = "red"
        ctx.textAlign = "center"
        ctx.fillText(f"{hours:02}:{minutes:02}:{seconds:02}", WIDTH / 2, HEIGHT / 2)

        js.requestAnimationFrame(create_proxy(update_countdown))

    js.requestAnimationFrame(create_proxy(update_countdown))

# Hàm nhập thời gian tùy ý
def set_target_time():
    now = datetime.now()
    # Thay đổi thời gian đích ở đây nếu muốn
    # Ví dụ: target_time = now + timedelta(seconds=30) # Đếm ngược 30 giây
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    print(f"Thời gian đếm ngược đến: {midnight.strftime('%Y-%m-%d %H:%M:%S')}")
    return midnight

# Đặt thời gian đích
target_time = set_target_time()

# Chạy countdown
countdown_to_target(target_time)