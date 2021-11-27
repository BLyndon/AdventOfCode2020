from functools import reduce


def loader(filename):
    with open('./puzzles/'+filename) as file:
        text = file.read()
    return text


def parser(text):
    def sub_parser(group):
        mask = group[0]
        savings = group[1:-1]
        parsed_group = []
        for saving in savings:
            mem, value = saving.split(" = ")
            value = int(value)
            mem = mem[:-1]
            mem = mem[4:]

            parsed_group.append([mask, mem, value])

        return parsed_group

    groups = text.split("mask = ")[1:]
    groups = list(map(lambda x: x.split("\n"), groups))
    groups = list(map(lambda x: sub_parser(x), groups))
    commands = []
    for group in groups:
        for writing in group:
            commands.append(writing)
    return commands


def solver_1(groups):
    def get_bin(num):
        num = bin(num).replace("0b", "")
        space = 36-len(num)
        space = space*"0"
        return space+num

    def mask(group):
        mask, _, num = group
        num = get_bin(num)
        for i in range(len(mask)):
            if mask[i] != 'X':
                num = num[:i] + mask[i] + num[i+1:]
        return int(num, 2)

    memory = dict()
    for group in groups:
        memory[group[1]] = mask(group)
    print(memory)
    return sum(list(memory.values()))


def solver_2(lines):
    return None


if __name__ == '__main__':
    filename = '14.txt'

    groups = parser(loader(filename))

    sol1 = solver_1(groups)
    sol2 = solver_2(groups)

    print("Part 1: {}".format(sol1))
    print("Part 2: {}".format(sol2))
