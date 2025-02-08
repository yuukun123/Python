# def putTwoPairInRoom(N, ls_pss):
#     rooms = [0] * N
#
#     for i in ls_pss:
#         index = 0
#         pss = i
#
#         while pss >= 2 and index < N:
#             if rooms[index] == 0 :
#                 rooms[index] = 2
#                 pss -= 2
#             index += 1
#
#         if pss == 1:
#             while index < N and rooms[index] != 0:
#                 index += 1
#             if index < N:
#                 rooms[index] = 1
#                 pss -= 1
#
#         index = 0
#         while pss > 0 and index < N:
#             if rooms[index] == 1:
#                 rooms[index] = 2
#                 pss -= 1
#             index += 1
#     print(', '.join(map(str, rooms)))

# cách khác
def putTwoPairInRoom(N, ls_pss):
    rooms = [0] * N
    index = 0

    for pss in ls_pss:
        # xếp khách vào phòng trống
        for _ in range(pss // 2): # lặp theo số cặp có trong đoàn khách
            while index < N and rooms[index] > 0:
                index += 1 # tìm phòng trống tiếp theo
            if index < N:
                rooms[index] = 2 # xếp 1 cặp khách vào phòng
                index += 1 # chuyển sang phòng tiếp theo
        # kiếm tra nếu có khách lẻ
        if pss % 2 == 1:
            place = False
            # tìm phòng trống trước
            for j in range(N):
                if rooms[j] == 0: # ưu tiên phòng trống
                    rooms[j] = 1
                    place = True
                    break
            # kiểm tra nếu không có phòng trống
            if not place:
                # duyệt lại từng phòng để tìm phòng nào có số nhỏ nhất mà chỉ có 1 khách
                for j in range(N):
                    if rooms[j] == 1: # tìm phòng chỉ có 1 khách
                        # thay thế số người trong phòn lên 2 người
                        rooms[j] = 2
                        break
    print(', '.join(map(str, rooms)))

N = int(input())
M = int(input())
ls_pss = [int(input()) for _ in range(M)]

putTwoPairInRoom(N, ls_pss)

