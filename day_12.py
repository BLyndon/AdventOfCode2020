class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = 'E'

    def manh_dist(self):
        return abs(self.x)+abs(self.y)

    def move(self, dir, value):
        if dir == 'N':
            self.x -= value
        elif dir == 'S':
            self.x += value
        elif dir == 'W':
            self.y -= value
        elif dir == 'E':
            self.y += value

    def rotate(self, value):
        directions = ['E', 'S', 'W', 'N']
        idx = (directions.index(self.dir)+int(value/90)) % 4
        self.dir = directions[idx]

    def navigate(self, instruction):
        action, value = instruction
        if action in ['N', 'S', 'E', 'W', 'F']:
            if action == 'F':
                dir = self.dir
            else:
                dir = action
            self.move(dir, value)
        elif action in ['R', 'L']:
            if action == 'R':
                self.rotate(value)
            else:
                self.rotate(-value)
        else:
            raise ValueError


def loader(filename):
    with open('./puzzles/'+filename) as file:
        lines = file.readlines()
    return lines


def parser(lines):
    lines = [line.replace("\n", "") for line in lines]
    instructions = [(line[0], int(line[1:])) for line in lines]
    return instructions


def solver_1(instructions):
    ship = Ship()
    for instruction in instructions:
        ship.navigate(instruction)
    return ship.manh_dist()


def solver_2(instructions):
    return None


#filename = '12_test.txt'
filename = '12.txt'

instructions = parser(loader(filename))

sol1 = solver_1(instructions)
sol2 = solver_2(instructions)

print("Part 1: {}".format(sol1))
print("Part 2: {}".format(sol2))
