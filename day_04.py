import re
import numpy as np


def loader(filename):
    with open('./puzzles/'+filename) as file:
        text = file.read()
    return text


def parser(text):
    batches = text.split("\n\n")

    batches = list(map(lambda x: x.replace("\n", " "), batches))
    kv_pairs = list(map(lambda x: x.split(" "), batches))
    return kv_pairs


def solver_1(kv_pairs):
    counter = 0
    for batch in kv_pairs:
        batch = set(map(lambda x: x[:3], batch))

        batch.add('cid')

        if len(batch) == 8:
            counter += 1

    return counter


def solver_2(kv_pairs):
    def isin(val, a, b):
        if val <= b and val >= a:
            return True
        else:
            return False

    def check_byr(val):
        return isin(int(val), 1920, 2002)

    def check_iyr(val):
        return isin(int(val), 2010, 2020)

    def check_eyr(val):
        return isin(int(val), 2020, 2030)

    def check_hgt(val):
        if len(val) < 3:
            return False
        unit = val[-2:]
        size = int(val[:-2])
        if unit == 'cm':
            return isin(size, 150, 193)
        if unit == 'in':
            return isin(size, 59, 76)

    def check_hcl(val):
        if re.search(r'^#([a-fA-F0-9]{6})$', val):
            return True
        else:
            return False

    def check_ecl(val):
        return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def check_pid(val):
        if re.search(r'^\d{9}$', val):
            return True
        else:
            return False

    counter = 0

    for batch in kv_pairs:
        if len(batch) < 7:
            continue

        batch = {kv.split(":")[0]: kv.split(":")[1] for kv in batch}

        if len(batch) == 7 and 'cid' in batch:
            continue

        checks = []
        checks.append(check_byr(batch['byr']))
        checks.append(check_iyr(batch['iyr']))
        checks.append(check_eyr(batch['eyr']))
        checks.append(check_hgt(batch['hgt']))
        checks.append(check_hcl(batch['hcl']))
        checks.append(check_pid(batch['pid']))
        checks.append(check_ecl(batch['ecl']))

        if np.asarray(checks).all():
            counter += 1

    return counter


#filename = '04_test.txt'
filename = '04.txt'

kv_pairs = parser(loader(filename))

sol1 = solver_1(kv_pairs)
sol2 = solver_2(kv_pairs)

print("Part 1: {}".format(sol1))
print("Part 2: {}".format(sol2))
