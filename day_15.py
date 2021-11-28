import numpy as np


def loader(filename):
    with open('./puzzles/'+filename) as file:
        text = file.read()
    return text


def parser(text):
    text = text.replace("\n", "").split(",")
    text = np.asarray(list(map(int, text)))
    return text


def solver_1(inp):
    for _ in range(len(inp), 2020):
        num = inp[-1]
        idx = np.argwhere(inp == num)
        if len(idx) > 1:
            idx = max(idx[:-1])
        diff = len(inp)-1-idx
        inp = np.append(inp, [diff])
    return inp[-1]


def solver_2(inp):
    pass


if __name__ == '__main__':
    #filename = '15_test.txt'
    filename = '15.txt'

    inp = parser(loader(filename))

    sol1 = solver_1(inp)
    sol2 = solver_2(inp)

    print("Part 1: {}".format(sol1))
    print("Part 2: {}".format(sol2))
