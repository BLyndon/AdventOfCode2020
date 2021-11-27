import numpy as np


def loader(filename):
    with open('./puzzles/'+filename) as file:
        lines = file.readlines()
    return lines


def parser(lines):
    def replacer(char):
        if char == '.':
            return 0
        elif char == 'L':
            return 1
        elif char == '#':
            return 2
    lines = [list(line.replace("\n", "")) for line in lines]
    state = np.asarray([list(map(lambda x: replacer(x), line))
                        for line in lines])
    return np.pad(state, 1, mode='constant')


def solver_1(state):
    def updater(x, y, state):
        if state[x, y] == 0:
            return 0
        else:
            dxdy = [[x-1, y], [x-1, y+1], [x, y+1], [x+1, y+1],
                    [x+1, y], [x+1, y-1], [x, y-1], [x-1, y-1]]
            if state[x, y] == 2:
                counter = 0
                for dx, dy in dxdy:
                    if state[dx, dy] == 2:
                        counter += 1
                if counter >= 4:
                    return 1
                else:
                    return 2
            elif state[x, y] == 1:
                for dx, dy in dxdy:
                    if state[dx, dy] == 2:
                        return 1
                return 2

    for _ in range(1000):
        prev_state = state.copy()
        for x in range(1, state.shape[0]-1):
            for y in range(1, state.shape[1]-1):
                state[x, y] = updater(x, y, prev_state)
        if (state == prev_state).all():
            break
    num_occ = int(np.sum(state[state == 2])/2)
    return num_occ


def solver_2(seats):
    return None


#filename = '11_test.txt'
filename = '11.txt'

state = parser(loader(filename))

sol1 = solver_1(state)
sol2 = solver_2(state)

print("Part 1: {}".format(sol1))
print("Part 2: {}".format(sol2))
