def read_file(filename) -> str:
    with open("dane.txt") as f:
        lines = f.readlines()
    text = "".join(lines)
    return text
