def loader(filename):
    with open('./puzzles/'+filename) as file:
        lines = file.readlines()
    return lines


def parser(lines):
    return [int(line) for line in lines]


def solver_1(nums):
    def sums(n, m):
        assert n >= m, ValueError
        sums = list()
        for i in range(n-m, n):
            for j in range(i+1, n):
                sums.append(nums[i]+nums[j])
        return sums
    m = 25
    for n in range(m+1, len(nums)):
        if nums[n] in sums(n, m):
            continue
        else:
            return nums[n]


def solver_2(lines):
    pass


if __name__ == '__main__':
    filename = '09.txt'

    nums = parser(loader(filename))

    sol1 = solver_1(nums)
    sol2 = solver_2(nums)

    print("Part 1: {}".format(sol1))
    print("Part 2: {}".format(sol2))
