import heapq
import math
from Node import Node
from Edge import Edge


# ---------------------------
# Lớp ghi log các bước của A*
# ---------------------------
class AStarLogger:
    def __init__(self):
        # Mỗi phần tử của steps là một dict chứa thông tin của 1 bước
        self.steps = []

    def log_step(self, step_number, current, neighbors_info, open_set, close_set):
        """
        Ghi lại thông tin của một bước:
         - step_number: số thứ tự bước
         - current: đỉnh p đang xử lý
         - neighbors_info: danh sách các dict chứa thông tin cập nhật của các đỉnh láng giềng q
         - open_set: danh sách các đỉnh đang có trong Open
         - close_set: danh sách các đỉnh đã được đưa vào Close
        """
        self.steps.append({
            "step": step_number,
            "current": current,
            "neighbors": neighbors_info,
            "open": sorted(open_set),
            "close": sorted(close_set)
        })

    def print_astar_table(self):
        """
        In bảng ASCII hiển thị các bước của thuật toán A*.
        Các cột gồm:
            Bước | Đỉnh p | Đỉnh q | g(q)=g(p)+cost(p,q) | f(q)=g(q)+h(q) | Open | Close
        """
        header = [
            "Bước",
            "Đỉnh p",
            "Đỉnh q",
            "g(q)=g(p)+cost(p,q)",
            "f(q)=g(q)+h(q)",
            "Open",
            "Close"
        ]
        table_rows = []
        for step_info in self.steps:
            step = step_info["step"]
            p = step_info["current"]
            open_str = ", ".join(map(str, step_info["open"]))
            close_str = ", ".join(map(str, step_info["close"]))
            if not step_info["neighbors"]:
                table_rows.append([
                    str(step),
                    str(p),
                    "-",
                    "-",
                    "-",
                    open_str,
                    close_str
                ])
            else:
                first_neighbor = True
                for nb in step_info["neighbors"]:
                    q = nb["q"]
                    g_str = nb["g_str"]
                    f_str = nb["f_str"]
                    if first_neighbor:
                        table_rows.append([
                            str(step),
                            str(p),
                            str(q),
                            g_str,
                            f_str,
                            open_str,
                            close_str
                        ])
                        first_neighbor = False
                    else:
                        table_rows.append([
                            "",
                            "",
                            str(q),
                            g_str,
                            f_str,
                            "",
                            ""
                        ])
        print_table_ascii(header, table_rows)


def print_table_ascii(header, rows):
    """
    Hàm in bảng ASCII với tiêu đề header và các dòng dữ liệu rows.
    """
    col_widths = [len(h) for h in header]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(cell))

    def print_row(row_data):
        line = "| " + " | ".join(f"{row_data[i]:<{col_widths[i]}}" for i in range(len(row_data))) + " |"
        print(line)

    def print_divider():
        line = "+-" + "-+-".join("-" * w for w in col_widths) + "-+"
        print(line)

    print_divider()
    print_row(header)
    print_divider()
    for row in rows:
        print_row(row)
    print_divider()


# ---------------------------
# Thuật toán A* với logging các bước
# ---------------------------
def AStar(start, end, adjList, heuristic):
    logger = AStarLogger()
    step_count = 0

    n = len(adjList)
    g = [math.inf] * n  # mảng lưu chi phí từ đỉnh xuất phát đến từng đỉnh
    f = [math.inf] * n  # mảng lưu giá trị f = g + h
    prev = [-1] * n  # mảng truy vết đường đi
    openSet = []  # PriorityQueue dùng heapq
    inOpenSet = {}  # Biến đánh dấu đỉnh có trong Open hay không
    inCloseSet = {}  # Biến đánh dấu đỉnh đã được duyệt

    # Khởi tạo đỉnh xuất phát
    g[start] = 0
    f[start] = heuristic[start]
    heapq.heappush(openSet, Node(start, f[start]))
    inOpenSet[start] = True

    while openSet:
        current = heapq.heappop(openSet).vertex
        inOpenSet[current] = False

        # Đưa đỉnh current vào Close trước khi xử lý láng giềng
        inCloseSet[current] = True

        neighbors_info = []

        if current == end:
            # Nếu đã đạt đích, ta log bước cuối nhưng set Open là rỗng
            logger.log_step(
                step_count, current, neighbors_info,
                [],  # Open set để trống vì không cần dùng nữa
                [k for k, v in inCloseSet.items() if v]
            )
            step_count += 1

            totalCost = g[end]
            path = []
            temp = current
            while temp != -1:
                path.append(temp)
                temp = prev[temp]
            path.reverse()
            print("Shortest path:", " ".join(map(str, path)))
            print("Path cost:", totalCost)

            logger.print_astar_table()
            return totalCost

        # Duyệt các láng giềng của current
        for edge in adjList[current]:
            neighbor = edge.to
            tentative_g = g[current] + edge.weight

            if not inCloseSet.get(neighbor, False) and tentative_g < g[neighbor]:
                prev[neighbor] = current
                g[neighbor] = tentative_g
                f[neighbor] = g[neighbor] + heuristic[neighbor]
                g_str = f"g({neighbor})=g({current})+{edge.weight}={g[current]}+{edge.weight}={tentative_g}"
                f_str = f"f({neighbor})=g({neighbor})+h({neighbor})={tentative_g}+{heuristic[neighbor]}={f[neighbor]}"
                neighbors_info.append({
                    "q": neighbor,
                    "g_str": g_str,
                    "f_str": f_str
                })
                if not inOpenSet.get(neighbor, False):
                    heapq.heappush(openSet, Node(neighbor, f[neighbor]))
                    inOpenSet[neighbor] = True

        # Ghi log thông tin của bước hiện tại
        logger.log_step(
            step_count, current, neighbors_info,
            [node.vertex for node in openSet],
            [k for k, v in inCloseSet.items() if v]
        )
        step_count += 1

    logger.print_astar_table()
    return -1  # Không tìm thấy đường đi

