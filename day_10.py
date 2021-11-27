import numpy as np


def loader(filename):
    with open('./puzzles/'+filename) as file:
        lines = file.readlines()
    return lines


def parser(lines):
    return np.asarray([int(x) for x in lines])


def solver_1(values):
    values_sorted = np.sort(values)
    differences = np.diff(values_sorted)

    n_1_jolts = len(differences[differences == 1])+1
    n_3_jolts = len(differences[differences == 3])+1

    return n_1_jolts*n_3_jolts


def solver_2(values):
    return None


#filename = '10_test.txt'
filename = '10.txt'

values = parser(loader(filename))

sol1 = solver_1(values)
sol2 = solver_2(values)

print("Part 1: {}".format(sol1))
print("Part 2: {}".format(sol2))
