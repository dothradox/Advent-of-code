def count_lines():
    return len(open("day3.txt").readlines())


def part1():
    gamma = ""
    epsilon = ""
    gamma_decimal = 0
    epsilon_decimal = 0

    # create a 2d-list
    list_2d = [None] * 12
    for i in range(12):
        list_2d[i] = [None] * count_lines()

    list_2d = [[None] * count_lines()] * 12

    f = open("day3.txt", "r")
    for line in f:
        for j in range(len(line)):
            list_2d[j][i] = line[j]

    for p in range(12):
        if list_2d[p].count("0") >= int(count_lines() / 2):
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    gamma_decimal = int(gamma, 2)
    epsilon_decimal = int(epsilon, 2)
    print(gamma_decimal, epsilon_decimal, gamma_decimal * epsilon_decimal)
    f.close()


part1()
