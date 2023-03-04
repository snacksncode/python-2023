with open("salaries.csv") as f:
    lines = f.readlines()[1:]
    for line in lines:
        print(line.split(","))
