def loader(filename):
    with open('./puzzles/'+filename) as file:
        lines = file.readlines()
    return lines


def parser(lines):
    timestamp = int(lines[0].replace("\n", ""))
    busses = lines[1].replace("\n", "").replace(",x", "").split(",")
    busses = [int(bus) for bus in busses]
    return timestamp, busses


def solver_1(input):
    timestamp, busses = input
    min_minutes = 1e10
    prod = 0
    for bus in busses:
        minutes = bus-timestamp % bus
        if minutes < min_minutes:
            min_minutes = minutes
            prod = min_minutes*bus
    return prod


def solver_2(lines):
    return None


#filename = '13_test.txt'
filename = '13.txt'

input = parser(loader(filename))

sol1 = solver_1(input)
sol2 = solver_2(input)

print("Part 1: {}".format(sol1))
print("Part 2: {}".format(sol2))
