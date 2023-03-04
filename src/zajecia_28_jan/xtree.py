def get_snail_trace(N: int) -> list[str]:
    result = []
    for x in range(N):
        green_leaves = 1 + x * 2
        leaves = ["*"] * green_leaves
        # print(leaves)
        total = -1 + 2 * N
        air_elements = total - green_leaves
        air_left = ["."] * (air_elements // 2)
        air_righ = ["."] * (air_elements // 2)
        line = air_left + leaves + air_righ
        s = "".join(line)
        result.append(s)
    return result


if __name__ == "__main__":
    for row in get_snail_trace(30):
        print(row)
