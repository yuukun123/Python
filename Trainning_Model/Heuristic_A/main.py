from AStarAlgorithm import AStar
from Edge import Edge

def main():
    try:
        with open("input.txt", "r") as f:
            data = f.read().split()
        """Tạo một iterator it từ danh sách data, cho phép ta lấy từng phần tử tuần tự bằng cách gọi next(it)."""
        it = iter(data)
        """
        Lần lượt lấy 4 giá trị đầu tiên từ iterator it, rồi chuyển chúng sang kiểu int.
        n là số đỉnh trong đồ thị (hoặc số đỉnh được đánh số đến n).
        
        m là số cạnh.
        
        s là đỉnh bắt đầu (start).
        
        t là đỉnh kết thúc (end).
        """
        n = int(next(it))
        m = int(next(it))
        s = int(next(it))
        t = int(next(it))

        """
        adjList = [[] for _ in range(n + 1)]: Tạo danh sách kề cho đồ thị, với n+1 danh sách rỗng (chỉ số từ 0 đến n).
        heuristic = [0] * (n + 1): Tạo danh sách heuristic có n+1 phần tử, khởi tạo bằng 0.
        """
        adjList = [[] for _ in range(n + 1)]
        heuristic = [0] * (n + 1)

        """
        Vòng lặp này lặp m lần, mỗi lần lấy 3 giá trị u, v, w (cũng bằng next(it))
        u và v là chỉ số đỉnh (tương ứng với một cạnh u -> v).
        w là trọng số (cost) của cạnh đó.
        adjList[u].append(Edge(v, w)): Thêm một đối tượng Edge(v, w) vào danh sách kề của đỉnh u. Qua đó, u có một cạnh đến v với trọng số w.
        """
        for _ in range(m):
            u = int(next(it))
            v = int(next(it))
            w = int(next(it))
            adjList[u].append(Edge(v, w))

        """
        Vòng lặp duyệt các chỉ số đỉnh từ 1 đến n (bỏ qua 0 nếu bạn không dùng).
        heuristic[i] = int(next(it)): Đọc giá trị heuristic tương ứng cho đỉnh i từ file và lưu vào mảng heuristic.
        """
        for i in range(1, n + 1):
            heuristic[i] = int(next(it))

        """
        Gọi hàm A* với tham số:
        s (đỉnh bắt đầu),
        t (đỉnh kết thúc),
        adjList (danh sách kề của đồ thị),
        heuristic (mảng heuristic của các đỉnh).
        Hàm AStar sẽ tiến hành tìm đường đi ngắn nhất (theo giải thuật A*) và có thể in ra kết quả (đường đi, chi phí, bảng, v.v. tùy bạn cài đặt).
        """
        AStar(s, t, adjList, heuristic)

        """
        Nếu quá trình open("input.txt") bị lỗi vì file không tồn tại hoặc không mở được, Python sẽ ném ra ngoại lệ FileNotFoundError. Khối except này sẽ bắt ngoại lệ đó và in ra thông báo lỗi.
        """
    except FileNotFoundError as e:
        print("Error opening input file:", e)


if __name__ == "__main__":
    main()

#dòng đầu tiên là số đỉnh - số cạnh - đỉnh start - đỉnh end
#dòng cuối cùng là h(đỉnh)
#các dòng ở giữa: đỉnh đầu - đỉnh cuối - trọng số

