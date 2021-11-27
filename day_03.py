def loader(filename):
    with open('./puzzles/'+filename) as file:
        lines = file.readlines()
    return lines


def parser(lines):
    return lines


def solver(lines, slope):
    n_lines = len(lines)
    prod = 1
    for m1, m2 in slope:
        counter = 0
        for i in range(1, n_lines):
            ii = m2*i
            if ii >= n_lines:
                break
            line = lines[ii][:-1]
            jj = (m1*i) % len(line)

            if line[jj] == '#':
                counter += 1
        prod *= counter

    return prod


#filename = '03_test.txt'
filename = '03.txt'

lines = parser(loader(filename))

slope1 = [[3, 1]]
slope2 = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

sol1 = solver(lines, slope1)
sol2 = solver(lines, slope2)

print("Part 1: {}".format(sol1))
print("Part 2: {}".format(sol2))
