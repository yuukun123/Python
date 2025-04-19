class TourResult:
    def __init__(self, tour, cost):
        self.tour = tour  # Danh sách các điểm đến trong tour
        self.cost = cost  # Tổng chi phí của tour


def find_tour(n, start_city, cost_matrix):
    visited = [False] * n
    start_index = start_city - 1
    current_city = start_index
    tour = [start_city]
    visited[current_city] = True
    total_cost = 0

    for _ in range(n - 1):
        next_city = -1
        min_cost = float('inf')

        for j in range(n):
            if not visited[j] and 0 <= cost_matrix[current_city][j] < min_cost:
                min_cost = cost_matrix[current_city][j]
                next_city = j

        if next_city == -1:
            print("Error: No valid next city found.")
            return TourResult([], float('inf'))

        tour.append(next_city + 1)
        total_cost += min_cost
        visited[next_city] = True
        current_city = next_city

    total_cost += cost_matrix[current_city][start_index]
    tour.append(start_city)

    return TourResult(tour, total_cost)


def find_best_tour(n, cost_matrix, start_points):
    best_tour = TourResult([], float('inf'))

    for start_city in start_points:
        if start_city < 1 or start_city > n:
            print(f"Invalid start city: {start_city}")
            continue

        current_tour = find_tour(n, start_city, cost_matrix)
        print(f"Tour from city {start_city}: {current_tour.tour} with cost {current_tour.cost}")

        if current_tour.cost < best_tour.cost:
            best_tour = current_tour

    return best_tour


if __name__ == "__main__":
    cost_matrix = [
        [0, 1, 2, 2, 4, 4],
        [4, 0, 1, 6, 10, 5],
        [8, 9, 0, 27, 9, 4],
        [7, 13, 10, 0, 8, 11],
        [7, 11, 25, 10, 0, 13],
        [4, 19, 4, 11, 10, 0]
    ]

    p = int(input("Nhập số lần chạy GTS1: "))
    if p < 1 or p > len(cost_matrix):
        print("Invalid input for p. Must be between 1 and", len(cost_matrix))
        exit()

    start_points = []
    print("Nhập các điểm xuất phát: ")
    for _ in range(p):
        v = int(input())
        if 1 <= v <= len(cost_matrix):
            start_points.append(v)
        else:
            print(f"Invalid start city: {v}")

    best_result = find_best_tour(len(cost_matrix), cost_matrix, start_points)

    print("\nBest Tour:", best_result.tour)
    print("Best Cost:", best_result.cost)
