import numpy as np


def loader(filename):
    with open('./puzzles/'+filename) as file:
        lines = file.readlines()
    return lines


def parser(lines):
    def line_parser(line):
        op, val = line.split(" ")

        if op == 'nop':
            op = 0
        elif op == 'acc':
            op = 1
        else:
            op = 2

        return op, int(val)

    lines = list(map(lambda line: line_parser(line), lines))

    return lines


def solver_1(lines):
    accumulator = 0
    memory = np.zeros(len(lines))
    i = 0

    while i < len(lines):
        if memory[i] == 1:
            break
        else:
            op, val = lines[i]
            if op == 0:
                memory[i] = 1
                i += 1
            elif op == 1:
                accumulator += val
                memory[i] = 1
                i += 1
            elif op == 2:
                memory[i] = 1
                i += val

    return accumulator


def solver_2(lines):
    pass


if __name__ == '__main__':
    filename = '08.txt'

    lines = parser(loader(filename))

    sol1 = solver_1(lines)
    sol2 = solver_2(lines)

    print("Part 1: {}".format(sol1))
    print("Part 2: {}".format(sol2))
