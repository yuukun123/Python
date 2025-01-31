import pygame
import sys
import random
from math import sin, cos, radians
from datetime import datetime, timedelta

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Countdown Timer with Fireworks")

# Màu sắc
PALETURQUOISE = (175, 238, 238)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_RED = (255, 150, 150)
RED = (255, 0, 0)  # Định nghĩa RED
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Phông chữ
font_large = pygame.font.Font(None, 80)  # Kích thước font lớn cho thời gian
font_medium = pygame.font.Font(None, 60)  # Kích thước font vừa cho "Countdown"

# Clock để giới hạn FPS
clock = pygame.time.Clock()

# Thêm nhạc nền
pygame.mixer.init()
pygame.mixer.music.load("wait.mp3")  # Nhạc chờ
pygame.mixer.music.set_volume(1.0)  # Điều chỉnh âm lượng (0.0 - 1.0)


# Lớp Particle (hạt pháo hoa)
class Particle:
    def __init__(self, x, y, angle, speed, color):
        self.x = x
        self.y = y
        self.vx = speed * cos(radians(angle))  # Tính tốc độ ngang dựa trên góc
        self.vy = speed * sin(radians(angle))  # Tính tốc độ dọc dựa trên góc
        self.color = color
        self.lifetime = random.randint(50, 120)  # Tuổi thọ của hạt

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.lifetime -= 1

    def draw(self, surface):
        if self.lifetime > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), 3)


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
            # Di chuyển pháo hoa lên
            self.y -= 5
            if self.y <= self.target_y:
                self.exploded = True
                self.create_particles()
        else:
            # Cập nhật các particle
            for particle in self.particles:
                particle.update()
            # Loại bỏ các particle đã "chết"
            self.particles = [p for p in self.particles if p.lifetime > 0]

    def create_particles(self):
        for angle in range(0, 360, 12):  # Tạo hạt theo hình tròn (30 hạt mỗi pháo hoa)
            speed = random.uniform(2, 5)  # Tốc độ ngẫu nhiên cho mỗi hạt
            self.particles.append(Particle(self.x, self.y, angle, speed, self.color))

    def draw(self, surface):
        if not self.exploded:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), 5)
        else:
            for particle in self.particles:
                particle.draw(surface)


# Hàm hiển thị Happy New Year và pháo bông trong 38 giây
def show_happy_new_year():
    pygame.mixer.music.stop()  # Dừng nhạc chờ
    pygame.mixer.music.load("hpny.mp3")  # Nhạc pháo bông
    pygame.mixer.music.play(-1)  # Phát nhạc pháo bông liên tục

    fireworks = [Firework() for _ in range(5)]  # Tạo 5 pháo hoa ban đầu
    end_time = datetime.now() + timedelta(seconds=38)  # Giới hạn thời gian 38 giây

    while datetime.now() < end_time:
        screen.fill(PALETURQUOISE)  # Làm sạch màn hình trước khi vẽ lại

        # Hiển thị chữ "Happy New Year" với viền và glow
        text = font_large.render("Happy New Year!", True, WHITE)
        glow_text = font_large.render("Happy New Year!", True, LIGHT_RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Đặt ở giữa màn hình

        # Vẽ glow (viền chữ màu đỏ nhạt)
        screen.blit(glow_text, text_rect.move(4, 4))  # Di chuyển nhẹ để tạo hiệu ứng glow

        # Vẽ chữ chính
        screen.blit(text, text_rect)

        # Cập nhật và vẽ pháo hoa
        for firework in fireworks:
            firework.update()
            firework.draw(screen)

        # Thêm pháo bông mới ngẫu nhiên
        if random.random() < 0.02:  # 2% cơ hội thêm pháo hoa mỗi frame
            fireworks.append(Firework())

        # Loại bỏ pháo bông không còn hoạt động
        fireworks = [fw for fw in fireworks if not fw.exploded or fw.particles]

        pygame.display.flip()

        # Kiểm tra sự kiện thoát
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)  # Giới hạn FPS

    pygame.mixer.music.stop()  # Dừng nhạc sau khi kết thúc pháo hoa


# Hàm tính thời gian còn lại đến thời điểm đích
def get_time_to_target(target_time):
    now = datetime.now()
    remaining = target_time - now
    return max(0, remaining.total_seconds())  # Trả về 0 nếu đã hết thời gian


# Hàm countdown
def countdown_to_target(target_time):
    # # Phát nhạc chờ trước khi bắt đầu đếm ngược
    # pygame.mixer.music.load("PyLearn/Learn/wait.mp3")  # Nhạc chờ
    # pygame.mixer.music.play(-1)  # Phát nhạc chờ liên tục

    # while True:
    #     # Tính thời gian còn lại
    #     remaining_seconds = get_time_to_target(target_time)
    #     if remaining_seconds <= 0:
    #         break

    #     hours = int(remaining_seconds // 3600)
    #     minutes = int((remaining_seconds % 3600) // 60)
    #     seconds = int(remaining_seconds % 60)

    #     # Làm sạch màn hình với nền PALETURQUOISE thay vì màu đen
    #     screen.fill(PALETURQUOISE)  # Sử dụng PALETURQUOISE làm nền

    #     # Hiển thị "Countdown" với bóng đổ
    #     countdown_text = font_medium.render("Countdown", True, WHITE)
    #     shadow_text = font_medium.render("Countdown", True, BLACK)  # Tạo bản sao chữ với màu đen

    #     # Vị trí chữ và bóng đổ
    #     countdown_rect = countdown_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    #     shadow_rect = shadow_text.get_rect(center=(WIDTH // 2 + 4, HEIGHT // 4 + 4))  # Dịch bóng đổ nhẹ

    #     # Vẽ bóng đổ (shadow)
    #     screen.blit(shadow_text, shadow_rect)

    #     # Vẽ chữ chính
    #     screen.blit(countdown_text, countdown_rect)

    #     # Hiển thị thời gian
    #     if remaining_seconds > 3:
    #         timer_text = font_large.render(f"{hours:02}:{minutes:02}:{seconds:02}", True, RED)
    #     else:
    #         timer_text = font_large.render(f"{seconds:02}", True, RED)

    #     text_rect = timer_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    #     # Vẽ thời gian
    #     screen.blit(timer_text, text_rect)

    #     pygame.display.flip()

    #     # Kiểm tra sự kiện thoát
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()

    #     clock.tick(30)

    # # Dừng nhạc chờ và phát nhạc pháo bông
    # pygame.mixer.music.stop()
    # show_happy_new_year()
    

    # Phát nhạc chờ trước khi bắt đầu đếm ngược
    pygame.mixer.music.load("wait.mp3")  # Nhạc chờ
    pygame.mixer.music.play(-1)  # Phát nhạc chờ liên tục

    while True:
        # Tính thời gian còn lại
        remaining_seconds = get_time_to_target(target_time)
        if remaining_seconds <= 0:
            break

        hours = int(remaining_seconds // 3600)
        minutes = int((remaining_seconds % 3600) // 60)
        seconds = int(remaining_seconds % 60)

        # Hiển thị thời gian đếm ngược trong terminal
        print(f"\rTime remaining: {hours:02}:{minutes:02}:{seconds:02}", end="")  # Dòng hiển thị trên terminal

        # Làm sạch màn hình với nền PALETURQUOISE thay vì màu đen
        screen.fill(PALETURQUOISE)  # Sử dụng PALETURQUOISE làm nền

        # Hiển thị "Countdown" với bóng đổ
        countdown_text = font_medium.render("Countdown", True, WHITE)
        shadow_text = font_medium.render("Countdown", True, BLACK)  # Tạo bản sao chữ với màu đen

        # Vị trí chữ và bóng đổ
        countdown_rect = countdown_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        shadow_rect = shadow_text.get_rect(center=(WIDTH // 2 + 4, HEIGHT // 4 + 4))  # Dịch bóng đổ nhẹ

        # Vẽ bóng đổ (shadow)
        screen.blit(shadow_text, shadow_rect)

        # Vẽ chữ chính
        screen.blit(countdown_text, countdown_rect)

        # Hiển thị thời gian
        if remaining_seconds > 3:
            timer_text = font_large.render(f"{hours:02}:{minutes:02}:{seconds:02}", True, RED)
        else:
            timer_text = font_large.render(f"{seconds:02}", True, RED)

        text_rect = timer_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Vẽ thời gian
        screen.blit(timer_text, text_rect)

        pygame.display.flip()

        # Kiểm tra sự kiện thoát
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(30)

    # Dừng nhạc chờ và phát nhạc pháo bông
    pygame.mixer.music.stop()
    show_happy_new_year()



# Hàm nhập thời gian tùy ý
def set_target_time():
    # print("Nhập thời gian đích (định dạng HH:MM:SS, mặc định là 1 phút):")
    # user_input = input("Thời gian đích (HH:MM:SS): ")
    # now = datetime.now()
    # if user_input:
    #     try:
    #         hours, minutes, seconds = map(int, user_input.split(":"))
    #         target_time = now + timedelta(hours=hours, minutes=minutes, seconds=seconds)
    #     except ValueError:
    #         print("Định dạng không hợp lệ! Sử dụng mặc định (1 phút).")
    #         target_time = now + timedelta(minutes=1)
    # else:
    #     print("Không nhập giá trị! Sử dụng mặc định (1 phút).")
    #     target_time = now + timedelta(minutes=1)

    # return target_time
    # now = datetime.now()
    # # target_time = now + timedelta(minutes=1)  # Thêm 1 phút vào thời gian hiện tại
    # return now
    
    # Hàm tự động lấy thời gian hiện tại và tính thời gian đến 12:00 CH (nửa đêm)
    now = datetime.now()  # Lấy thời gian hiện tại
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1, seconds=1)  # 12:00 CH + 1 giây

    print(f"Thời gian đếm ngược đến: {midnight.strftime('%Y-%m-%d %H:%M:%S')}")  # In thời gian đích
    return midnight


# # Hàm lấy đúng thời gian hiện tại
# def set_target_time():
#     now = datetime.now()  # Lấy thời gian hiện tại
#     print(f"Thời gian đếm ngược đến: {now.strftime('%H:%M:%S')}")  # Hiển thị thời gian hiện tại
#     return now  # Trả về thời gian hiện tại




# Đặt thời gian đích
target_time = set_target_time()

# Chạy countdown
countdown_to_target(target_time)

# Thoát Pygame
pygame.quit()
