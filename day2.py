def count_lines():
    return len(open("day2.txt").readlines())


def part1():
    f = open("day2.txt", "r")
    horizontal_position = 0
    depth = 0
    for i in range(count_lines()):
        line = f.readline().strip()
        if line[0] == "f":
            horizontal_position += int(line[-1])
        elif line[0] == "u":
            depth -= int(line[-1])
        else:
            depth += int(line[-1])
    return horizontal_position * depth


def part2():
    f = open("day2.txt", "r")
    horizontal_position = 0
    depth = 0
    aim = 0
    for i in range(count_lines()):
        line = f.readline().strip()
        if line[0] == "f":
            horizontal_position += int(line[-1])
            depth += aim * int(line[-1])

        elif line[0] == "u":
            aim -= int(line[-1])
        else:
            aim += int(line[-1])

    return horizontal_position * depth


print("Answer to part 1:", part1())
print("Answer to part 2:", part2())
