def get_board(n: int) -> list[list[str]]:
    row = ["."] * n
    board = [row.copy() for i in range(n)]
    return board


b = get_board(5)
b[0][0] = "x"
print(b)

if __name__ == "__main__":
    N = 10
    b = get_board(N)
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    t = 0
    position = [0, 0]
    for _ in range(500):
        new_pos = [0, 0]
        new_pos[0] = position[0] + moves[t][0]
        new_pos[1] = position[1] + moves[t][1]
        if new_pos[0] >= N or new_pos[0] < 0:
            t = (t + 1) % 4
            continue
        if new_pos[1] >= N or new_pos[1] < 0:
            t = (t + 1) % 4
            continue
        position = new_pos
        b[position[0]][position[1]] = "#"

    for row in b:
        print("".join(row))
