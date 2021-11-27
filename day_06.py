def loader(filename):
    with open('./puzzles/'+filename) as file:
        text = file.read()
    return text


def parser(text):
    return text.split("\n\n")


def solver_1(groups):
    groups = list(map(lambda x: x.replace("\n", ""), groups))
    groups = list(map(lambda x: [a for a in x], groups))
    groups = list(map(lambda x: len(set(x)), groups))

    return sum(groups)


def solver_2(groups):
    groups = [x.split("\n") for x in groups]
    groups = [[{answer for answer in person}
               for person in group] for group in groups]
    groups = [group[0].intersection(*group) for group in groups]
    groups = list(map(lambda x: len(set(x)), groups))
    return sum(groups)


#filename = '06_test.txt'
filename = '06.txt'

lines = parser(loader(filename))

sol1 = solver_1(lines)
sol2 = solver_2(lines)

print("Part 1: {}".format(sol1))
print("Part 2: {}".format(sol2))
