import random
import pygame
import json
import os
from datetime import datetime

# Khởi tạo pygame mixer để phát nhạc
pygame.mixer.init()

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
playerInfo = {}  # Lưu trữ thông tin của tất cả người chơi
current_player = None  # Tên của người chơi hiện tại

bots = {
    "Bot1": {"balance": 500},
    "Bot2": {"balance": 500},
    "Bot3": {"balance": 500},
}

MIN_BET = 50  # Số tiền cược tối thiểu

# Lưu lịch sử trò chơi
game_history = []

# Biến flag để kiểm tra xem nhạc đã được phát chưa
music_playing = False

def play_background_music():
    global music_playing
    if not music_playing:  # Kiểm tra nếu nhạc chưa được phát
        pygame.mixer.music.load('music.mp3')  # Tải nhạc nền (đảm bảo có file 'music.mp3' trong thư mục)
        pygame.mixer.music.set_volume(0.5)  # Đặt âm lượng nhạc nền
        pygame.mixer.music.play(-1, 0.0)  # Phát nhạc nền lặp lại vô hạn
        music_playing = True  # Đánh dấu là nhạc đã phát

def stop_background_music():
    global music_playing
    if music_playing:  # Dừng nhạc nếu đang phát
        pygame.mixer.music.stop()
        music_playing = False  # Đánh dấu nhạc đã dừng

# Khởi tạo dữ liệu cho admin (chỉ thực hiện khi file admin_data.json chưa tồn tại)
def initialize_admin():
    if not os.path.exists("admin_data.json"):
        admin_info = {
            "admin": {
                "password": "admin123",  # Mật khẩu mặc định cho admin, có thể thay đổi sau khi đăng nhập
                "balance": 10000  # Số dư mặc định cho admin
            }
        }
        with open("admin_data.json", "w") as f:
            json.dump(admin_info, f, indent=4)
        print("Admin account initialized with default credentials.")
    else:
        print("Admin data file already exists.")


# Đọc dữ liệu admin từ file, thêm xử lý lỗi nếu file không hợp lệ
def load_admin_data():
    try:
        if os.path.exists("admin_data.json"):
            with open("admin_data.json", "r") as f:
                return json.load(f)
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Error reading admin data: {e}")
    return {}  # Nếu không đọc được, trả về dữ liệu mặc định (rỗng)

# Cập nhật thông tin admin vào file
def save_admin_data(admin_data):
    with open("admin_data.json", "w") as f:
        json.dump(admin_data, f, indent=4)

# Đọc và lưu dữ liệu từ file
def load_data():
    global playerInfo, game_history
    if os.path.exists("player_data.json"):
        with open("player_data.json", "r") as f:
            playerInfo = json.load(f)
    if os.path.exists("game_history.json"):
        with open("game_history.json", "r") as f:
            game_history = json.load(f)


def save_data():
    with open("player_data.json", "w") as f:
        json.dump(playerInfo, f, indent=4)
    with open("game_history.json", "w") as f:
        json.dump(game_history, f, indent=4)


def threeClaws():
    sum_values = 0  # Tổng giá trị của các lá bài

    print("Lá bài được chọn:", end=' ')
    for _ in range(3):
        card = cards[random.randint(0, len(cards) - 1)]  # Chọn lá bài ngẫu nhiên
        print(card, end=' ')

        # Gán giá trị số cho lá bài
        if card in ['J', 'Q', 'K']:
            value = 10
        elif card == 'A':
            value = 1
        else:
            value = int(card)

        sum_values += value  # Cộng dồn giá trị

    # Tính tổng modulo 10
    final_sum = sum_values % 10
    print()
    print("-> Tổng giá trị: ", final_sum)
    print()
    return final_sum


def placeBet(player_name):
    global current_player
    if player_name == current_player:  # Đặt cược cho người chơi hiện tại
        bet = int(input(f"Enter the amount you want to bet (minimum {MIN_BET}): "))
        if bet < MIN_BET:
            print(f"The minimum bet is {MIN_BET}.")
            return placeBet(player_name)
        elif bet <= playerInfo[current_player]["balance"]:
            playerInfo[current_player]["balance"] -= bet
            print(f"{current_player} placed a bet of {bet}. Remaining balance: {playerInfo[current_player]['balance']}")
            return bet
        else:
            print("You don't have enough balance.")
            return 0
    else:  # Đặt cược cho bot
        if bots[player_name]["balance"] < MIN_BET:
            print(f"{player_name} does not have enough balance to place the minimum bet.")
            return 0
        bet = random.randint(MIN_BET, min(100, bots[player_name]["balance"]))  # Số tiền cược của bot
        bots[player_name]["balance"] -= bet
        print(f"{player_name} placed a bet of {bet}. Remaining balance: {bots[player_name]['balance']}")
        return bet

def play():
    global current_player
    if current_player:
        while True:  # Thêm vòng lặp để người chơi có thể chơi liên tục
            print("\nStarting game...")
            player_bet = placeBet(current_player)  # Người chơi đặt cược
            if player_bet == 0:
                return

            # Các bot đặt cược
            bot1_bet = placeBet("Bot1")
            bot2_bet = placeBet("Bot2")
            bot3_bet = placeBet("Bot3")

            # Tính điểm
            player_score = threeClaws()
            bot1_score = threeClaws()
            bot2_score = threeClaws()
            bot3_score = threeClaws()

            scores = {
                current_player: player_score,
                "Bot1": bot1_score,
                "Bot2": bot2_score,
                "Bot3": bot3_score,
            }

            bets = {
                current_player: player_bet,
                "Bot1": bot1_bet,
                "Bot2": bot2_bet,
                "Bot3": bot3_bet,
            }

            # Xác định người thắng
            max_score = max(scores.values())
            winners = [name for name, score in scores.items() if score == max_score]

            print(f"\nScores: {scores}")
            print(f"Bets: {bets}\n")

            if len(winners) > 1:
                print(f"It's a tie between {', '.join(winners)}!")
                # Tiền cược được trả lại cho mỗi người thua (trừ 2%)
                for name, bet in bets.items():
                    refund = bet * 0.98
                    if name == current_player:
                        playerInfo[name]["balance"] += refund
                    else:
                        bots[name]["balance"] += refund
                    print(f"{name} gets a refund of {refund:.2f} (after 2% fee).")
            else:
                winner = winners[0]
                print(f"{winner} wins!")
                total_pot = 0

                # Người thua đóng góp tiền cược và thêm 5% phí
                for name, bet in bets.items():
                    if name != winner:
                        contribution = bet * 1.05
                        total_pot += contribution
                        print(f"{name} contributed {contribution:.2f} (5% fee included).")
                print(f"Total pot for {winner}: {total_pot:.2f}")

                # Cộng tiền thắng cho người thắng
                if winner == current_player:
                    playerInfo[winner]["balance"] += total_pot
                else:
                    bots[winner]["balance"] += total_pot

            # Lưu lịch sử trò chơi với thông tin lần chơi và thời gian
            game_number = len(game_history) + 1  # Số lần chơi (lần chơi tiếp theo)
            game_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Lấy thời gian hiện tại
            game_history.append({
                "game_number": game_number,
                "time": game_time,
                "players": scores,
                "bets": bets,
                "winner": winners[0],
            })

            # Hiển thị số dư sau trận đấu
            print("\nFinal balances:")
            print(f"{current_player}: {playerInfo[current_player]['balance']}")
            for bot_name, bot_data in bots.items():
                print(f"{bot_name}: {bot_data['balance']}")

            # Hỏi người chơi có muốn chơi tiếp không
            continue_game = input("\nDo you want to play again? (y/n): ")
            if continue_game.lower() != 'y':
                break  # Nếu người chơi không muốn chơi tiếp, thoát khỏi vòng lặp và quay lại menu

    else:
        print("You need to login to play!")



# Đăng xuất
def logout():
    global current_player
    print(f"Goodbye, {current_player}!")
    current_player = None  # Đặt lại người chơi hiện tại là None (đăng xuất)
    menu()  # Quay lại menu chính

# Đăng nhập
def login():
    global current_player
    name = input("Player name: ")
    password = input("Password: ")

    # Kiểm tra tài khoản admin
    admin_data = load_admin_data()
    if name == "admin" and password == admin_data.get("admin", {}).get("password"):
        current_player = name
        print(f"Welcome, Admin!")
        admin_menu()  # Hiển thị menu cho admin khi đăng nhập thành công
        return

    # Kiểm tra tài khoản người chơi
    if name in playerInfo and playerInfo[name].get("password") == password:
        current_player = name
        print(f"Welcome, {current_player}!")
        player_menu()  # Hiển thị menu cho người chơi khi đăng nhập thành công
    else:
        print("Invalid username or password.")


def signup():
    name = input("Player name: ")
    if name in playerInfo:
        print("Player name already exists.")
    else:
        password = input("Password: ")
        balance = int(input("Initial deposit amount: "))
        playerInfo[name] = {"password": password, "balance": balance}
        print("Signup successful!")


# 3. Thay đổi mật khẩu
def change_password():
    global current_player
    if current_player:
        old_password = input("Enter your old password: ")
        if playerInfo[current_player]["password"] == old_password:
            new_password = input("Enter your new password: ")
            confirm_password = input("Confirm your new password: ")
            if new_password == confirm_password:
                playerInfo[current_player]["password"] = new_password
                save_data()
                print("Password changed successfully.")
            else:
                print("Passwords do not match.")
        else:
            print("Incorrect old password.")
    else:
        print("You need to login first.")


# 4. Lịch sử trò chơi
def view_game_history():
    if game_history:
        print("\nGame History:")
        for game in game_history:
            # Kiểm tra sự tồn tại của các khóa cần thiết
            game_number = game.get('game_number', 'N/A')
            game_time = game.get('time', 'N/A')
            print(f"Game {game_number} - Time: {game_time}")
            print(f"Players: {game['players']}")
            print(f"Bets: {game['bets']}")
            print(f"Winner: {game['winner']}\n")
    else:
        print("No game history available.")

# Hàm xem thông tin tất cả người chơi (chỉ dành cho admin)
def view_all_players_info():
    if current_player == "admin":
        print("\nAll Players Information:")
        for player_name, player_data in playerInfo.items():
            print(f"Player: {player_name}")
            print(f"Balance: {player_data['balance']}")
            print("-" * 30)
    else:
        print("You need to be an admin to view all player information.")

# 5. Xem thông tin người chơi
def see_player_info():
    if current_player:
        print(f"Player Info: ")
        print(f"Name: {current_player}")
        print(f"Balance: {playerInfo[current_player]['balance']}")
    else:
        print("You need to login first.")

# Menu cho người chơi đã đăng nhập
def player_menu():
    print("\nWelcome to the Three Claws Casino!")
    while True:
        print("\n1. Play Game\n2. View Game History\n3. Change Password\n4. See Player Info\n5. Logout")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            play()
        elif choice == 2:
            view_game_history()
        elif choice == 3:
            change_password()
        elif choice == 4:
            see_player_info()
        elif choice == 5:
            logout()
            break
        else:
            print("Invalid choice. Please try again.")

# Menu cho admin đã đăng nhập
def admin_menu():
    print("\nWelcome, Admin!")
    while True:
        print("\n1. View All Players Info (Admin)\n2. Logout")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            view_all_players_info()  # Admin xem thông tin tất cả người chơi
        elif choice == 2:
            logout()
            break
        else:
            print("Invalid choice. Please try again.")



# Menu chính
def menu():
    while True:
        print("\nWelcome to the Three Claws Casino!")
        print("\n1. Login\n2. Signup\n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            login()
        elif choice == 2:
            signup()
        elif choice == 3:
            print("Goodbye!")
            stop_background_music()  # Dừng nhạc nền khi thoát
            save_data()  # Lưu dữ liệu khi thoát
            exit()
        else:
            print("Invalid choice. Please try again.")

# Main block
if __name__ == "__main__":
    initialize_admin()  # Thực thi hàm để khởi tạo tài khoản admin khi chương trình bắt đầu
    load_data()  # Tải dữ liệu khi bắt đầu chương trình
    play_background_music()  # Bắt đầu phát nhạc nền khi chạy chương trình
    menu()  # Hiển thị menu chính

