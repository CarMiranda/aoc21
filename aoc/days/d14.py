import pathlib
from collections import Counter


def parse_input(filepath: pathlib.Path):
    with open(filepath) as f:
        chunks = f.read().rstrip().split("\n\n")
    polymer = chunks[0]
    rules = [entry.rstrip().split(" -> ") for entry in chunks[1].split("\n")]
    rules = {pred: pred[0] + insert + pred[1] for pred, insert in rules}

    return polymer, rules


def part_one(filepath: pathlib.Path):
    polymer, rules = parse_input(filepath)
    for step in range(10):
        s = ""
        for i in range(len(polymer)):
            mer = polymer[i : i + 2]
            s += rules.get(mer, mer)[:-1]
        polymer = s + mer[-1]

    cnt = Counter(polymer)
    return cnt.most_common(1)[0][1] - cnt.most_common()[-1][1]


def part_two(filepath: pathlib.Path):
    polymer, rules = parse_input(filepath)
    counter = {polymer[i : i + 2]: 0 for i in range(len(polymer))}
    for i in range(len(polymer)):
        counter[polymer[i : i + 2]] += 1

    for step in range(40):
        new_counter = dict()
        for mer, k in counter.items():
            new_mer = rules.get(mer, mer)
            if len(new_mer) == 3:
                m1, m2 = new_mer[:2], new_mer[1:]
                new_counter[m1] = new_counter.get(m1, 0) + k
                new_counter[m2] = k + new_counter.get(m2, 0)
            elif len(new_mer) == 2:
                new_counter[new_mer] = k
        counter = new_counter

    ccounter = dict()
    for key, val in counter.items():
        c1, c2 = key
        ccounter[c1] = ccounter.get(c1, 0) + val

    ccounter[polymer[-1]] += 1
    vmax = 0
    vmin = ccounter[polymer[-1]]
    for k, v in ccounter.items():
        if v > vmax:
            vmax = v
        if v < vmin:
            vmin = v

    return vmax - vmin
