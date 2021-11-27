def loader(filename):
    with open('./puzzles/'+filename) as file:
        lines = file.readlines()
    return lines


def parser(lines):
    parsed_lines = list()
    for line in lines:
        line = line.replace("\n", "")
        code, pw = line.split(': ')
        letter = code[-1]
        a, b = code[:-2].split('-')
        a, b = int(a), int(b)
        parsed_lines.append([a, b, letter, pw])
    return parsed_lines


def solver_1(lines):
    counter = 0
    for line in lines:
        a, b, letter, pw = line
        s = sum([letter == i for i in pw])
        if a <= s and s <= b:
            counter += 1
    return counter


def solver_2(lines):
    counter = 0
    for line in lines:
        a, b, letter, pw = line
        s = sum([letter == pw[i-1] for i in [a, b]])
        if s == 1:
            counter += 1
    return counter


#filename = '02_test.txt'
filename = '02.txt'

lines = parser(loader(filename))

sol1 = solver_1(lines)
sol2 = solver_2(lines)

print("Part 1: {}".format(sol1))
print("Part 2: {}".format(sol2))
