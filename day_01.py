def loader(filename):
    with open('./puzzles/'+filename) as file:
        lines = file.readlines()
    return lines


def parser(lines):
    return [int(line) for line in lines]


def solver_1(lines):
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            if lines[i]+lines[j] == 2020:
                return lines[i]*lines[j]


def solver_2(lines):
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            for k in range(j+1, len(lines)):
                if lines[i]+lines[j]+lines[k] == 2020:
                    return lines[i]*lines[j]*lines[k]


#filename = '01_test.txt'
filename = '01.txt'

lines = parser(loader(filename))

sol1 = solver_1(lines)
sol2 = solver_2(lines)

print("Part 1: {}".format(sol1))
print("Part 2: {}".format(sol2))
