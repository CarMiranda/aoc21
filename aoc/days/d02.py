import pathlib


def parse_input(filepath: pathlib.Path):
    with open(filepath) as f:
        dirs = [line.rstrip().split(" ") for line in f.readlines()]

    return dirs


def trad1(orientation: str, magnitude: int):
    if orientation == "forward":
        return (magnitude, 0)
    elif orientation == "up":
        return (0, -magnitude)
    elif orientation == "down":
        return (0, magnitude)


def trad2(orientation: str, magnitude: int, aim: int):
    if orientation == "forward":
        return (magnitude, magnitude * aim, 0)
    elif orientation == "up":
        return (0, 0, -magnitude)
    elif orientation == "down":
        return (0, 0, magnitude)


def part_one(filepath: pathlib.Path):
    dirs = parse_input(filepath)
    x, y = 0, 0
    for o, m in dirs:
        xx, yy = trad1(o, int(m))
        x += xx
        y += yy
    return x * y


def part_two(filepath: pathlib.Path):
    dirs = parse_input(filepath)
    x, y, a = 0, 0, 0
    for o, m in dirs:
        xx, yy, aa = trad2(o, int(m), a)
        x += xx
        y += yy
        a += aa
    return x * y
