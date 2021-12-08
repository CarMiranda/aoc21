import pathlib


def parse_input(filepath: pathlib.Path):
    with open(filepath) as f:
        raw_bits = [line.rstrip() for line in f.readlines()]
        bits = [list(b) for b in raw_bits]
        bits = list(zip(*bits))

    return raw_bits, bits


def part_one(filepath: pathlib.Path):

    raw_bits, bits = parse_input(filepath)

    n_bits = len(bits)
    llen = len(bits[0])
    cnts = [0] * n_bits
    s = ""
    for i in range(n_bits):
        b = list(map(int, bits[i]))
        cnts[i] = sum(b)
        s += "0" if cnts[i] < llen // 2 else "1"

    most_common = int(s, 2)
    s = s.replace("0", "2").replace("1", "0").replace("2", "1")
    least_common = int(s, 2)

    return most_common * least_common


def part_two(filepath: pathlib.Path):

    raw_bits, bits = parse_input(filepath)

    n_bits = len(bits)
    o2_idx = list(range(len(bits[0])))
    co2_idx = list(range(len(bits[0])))

    for i in range(n_bits):
        b = list(map(int, bits[i]))

        if len(o2_idx) > 1:
            b_o2 = [b[i] for i in o2_idx if i in o2_idx]
            c_o2 = int(sum(b_o2) * 2 >= len(b_o2))
            o2_idx = [j for i, j in enumerate(o2_idx) if b_o2[i] == c_o2]

        if len(co2_idx) > 1:
            b_co2 = [b[i] for i in co2_idx if i in co2_idx]
            c_co2 = int(sum(b_co2) * 2 >= len(b_co2))
            co2_idx = [j for i, j in enumerate(co2_idx) if b_co2[i] != c_co2]

    return int(raw_bits[o2_idx[-1]], 2) * int(raw_bits[co2_idx[-1]], 2)
