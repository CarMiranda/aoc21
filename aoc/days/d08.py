import pathlib


def parse_input(filepath: pathlib.Path):
    with open(filepath) as f:
        inputs, outputs = list(
            zip(*[entry.rstrip().split(" | ") for entry in f.readlines()])
        )

    inputs = [i.split(" ") for i in inputs]
    outputs = [o.split(" ") for o in outputs]

    return inputs, outputs


def part_one(filepath: pathlib.Path):
    inputs, outputs = parse_input(filepath)

    cnt = {i: 0 for i in range(10)}
    for ns in outputs:
        for n in ns:
            if len(n) in [2, 4, 3, 7]:
                cnt[len(n)] += 1

    return sum(cnt.values())


def part_two(filepath: pathlib.Path):

    inputs, outputs = parse_input(filepath)
    results = []
    for ns, outs in zip(inputs, outputs):
        lens = list(map(len, ns))
        sets = list(map(set, ns))
        one = sets[lens.index(2)]
        four = sets[lens.index(4)]
        seven = sets[lens.index(3)]
        eight = sets[lens.index(7)]

        bd = four.difference(one)

        # Searching for 0, 6 and 9 (length 6) using c, f difference
        tmp = [i for i, length in enumerate(lens) if length == 6]
        for i in tmp:
            if not bd.issubset(sets[i]):
                zero = sets[i]
                d = bd.difference(sets[i])
                b = bd.difference(d)
            elif not one.issubset(sets[i]):
                six = sets[i]
            else:
                nine = sets[i]

        # Searching for 2, 3 and 5 using b, c, f differences
        tmp = [i for i, length in enumerate(lens) if length == 5]
        three = None
        for i in tmp:
            if one.issubset(sets[i]):
                three = sets[i]
            elif not b.issubset(sets[i]):
                if not bd.issubset(sets[i]):
                    two = sets[i]
            else:
                five = sets[i]

        out = ""
        outs = [set(o) for o in outs]
        for o in outs:
            if o == one:
                out += "1"
            elif o == two:
                out += "2"
            elif o == three:
                out += "3"
            elif o == four:
                out += "4"
            elif o == five:
                out += "5"
            elif o == six:
                out += "6"
            elif o == seven:
                out += "7"
            elif o == eight:
                out += "8"
            elif o == nine:
                out += "9"
            elif o == zero:
                out += "0"

        results.append(int(out))

    return sum(results)
