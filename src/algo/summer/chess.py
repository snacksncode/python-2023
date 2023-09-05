import re
import matplotlib.pyplot as plt
import random


def is_valid_input(input_str):
    return bool(re.match(r"^[a-hA-H][1-8]$", input_str))


def get_random_point():
    columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
    row = random.randint(1, 8)
    column = random.choice(columns)
    return column + str(row)


def get_possible_moves(x, y):
    moves = []
    possible_moves = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    ]
    for dx, dy in possible_moves:
        new_x = x + dx
        new_y = y + dy
        if 1 <= new_x <= 8 and 1 <= new_y <= 8:
            moves.append((new_x, new_y))
    return moves


def calculate_moves(from_point, to_point):
    visited = {from_point}
    queue = [(from_point, 0, [from_point])]

    while queue:
        current_point, moves_count, moves_history = queue.pop(0)
        if current_point == to_point:
            return moves_count, moves_history

        x, y = current_point
        possible_moves = get_possible_moves(x, y)

        for move in possible_moves:
            if move not in visited:
                visited.add(move)
                queue.append((move, moves_count + 1, moves_history + [move]))

    return None, []


while True:
    start_point = input("Podaj punkt początkowy (np. a1, random): ")
    end_point = input("Podaj punkt docelowy (np. c3, random): ")

    if start_point == "random":
        start_point = get_random_point()

    if end_point == "random":
        end_point = get_random_point()

    if is_valid_input(start_point) and is_valid_input(end_point):
        break
    else:
        print("Niepoprawny format pola. Wprowadź ponownie.")

start_x = ord(start_point[0].lower()) - ord("a") + 1
start_y = int(start_point[1])
end_x = ord(end_point[0].lower()) - ord("a") + 1
end_y = int(end_point[1])

moves_count, moves_history = calculate_moves((start_x, start_y), (end_x, end_y))

if moves_count is None:
    print("Nie można dotrzeć z punktu A do punktu B.")
else:
    print(
        f"Liczba ruchów potrzebnych do dotarcia z {start_point} do {end_point}: {moves_count}"
    )

    fig, ax = plt.subplots()

    for i in range(9):
        for j in range(9):
            if (i + j) % 2 == 0:
                color = "white"
            else:
                color = "black"
            ax.add_patch(plt.Rectangle((i, j), 1, 1, color=color))

    for idx, move in enumerate(moves_history):
        color = "blue"
        if idx == 0:
            color = "green"
        if idx == len(moves_history) - 1:
            color = "red"

        ax.add_patch(plt.Rectangle((move[0] - 1, move[1] - 1), 1, 1, color=color))
        ax.text(
            move[0] + 0.5 - 1,
            move[1] + 0.5 - 1,
            idx,
            ha="center",
            va="center",
            color="white",
            fontsize=12,
            fontweight="bold",
        )

    ax.set_xticks([0.5 + i for i in range(9)])
    ax.set_yticks([0.5 + i for i in range(9)])
    ax.set_xticklabels(["a", "b", "c", "d", "e", "f", "g", "h", ""])
    ax.set_yticklabels(["1", "2", "3", "4", "5", "6", "7", "8", ""])

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)

    ax.set_aspect("equal")

    plt.title(f"Ruchy skoczka z {start_point} do {end_point}")
    plt.show()
