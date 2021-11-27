import numpy as np


def loader(filename):
    with open('./puzzles/'+filename) as file:
        lines = file.readlines()
    return lines


def parser(lines):
    return [line.replace("\n", "") for line in lines]


def solver_1(lines):
    def divide(arr, bin):
        mid = int(len(arr)/2)
        if bin == 'F' or bin == 'L':
            return arr[:mid]
        else:
            return arr[mid:]

    def get_num(str):
        pow = len(str)
        num = np.arange(0, 2**pow)
        for bin in str:
            num = divide(num, bin)
        return num[0]

    ids = []
    for line in lines:
        row_code = line[:7]
        col_code = line[7:]

        row = get_num(row_code)
        col = get_num(col_code)

        id = row*8+col

        ids.append(id)

    return ids


def solver_2(ids):
    ids.sort()
    for i in range(len(ids)-1):
        if ids[i]+2 == ids[i+1]:
            return ids[i]+1


filename = '05.txt'

lines = parser(loader(filename))

ids = solver_1(lines)
sol2 = solver_2(ids)
sol1 = max(ids)

print("Part 1: {}".format(sol1))
print("Part 2: {}".format(sol2))
