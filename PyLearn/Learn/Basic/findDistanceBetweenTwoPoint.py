def findDistanceBetweenTwoPoint(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5

distance = findDistanceBetweenTwoPoint([15, 7], [22, 11])
print(f"{distance:.2f}")
