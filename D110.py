def min_king_moves(start, end):
    x1 = ord(start[0]) - ord('a')
    y1 = int(start[1]) - 1
    x2 = ord(end[0]) - ord('a')
    y2 = int(end[1]) - 1
    return max(abs(x1 - x2), abs(y1 - y2))
start = input().strip()
end = input().strip()
steps = min_king_moves(start, end)
print(steps)
