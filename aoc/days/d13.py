import pathlib


def parse_input(filepath: pathlib.Path):
    with open(filepath) as f:
        chunks = f.read().rstrip().split("\n\n")
        points = set(
            [
                tuple(map(int, point.rstrip().split(",")))
                for point in chunks[0].split("\n")
            ]
        )
        instructions = [
            parse_instruction(instruction) for instruction in chunks[1].split("\n")
        ]

    return points, instructions


def parse_instruction(instruction):
    orientation, value = instruction.rstrip().split(" ")[-1].split("=")

    return orientation, int(value)


def fold_once(points, orientation, value):

    if orientation == "x":
        folded = set()
        for x, y in points:
            if x < value:
                folded.add((x, y))
            elif x <= 2 * value:
                folded.add((2 * value - x, y))
    if orientation == "y":
        folded = set()
        for x, y in points:
            if y < value:
                folded.add((x, y))
            elif y <= 2 * value:
                folded.add((x, 2 * value - y))

    return folded


def part_one(filepath: pathlib.Path):
    points, instructions = parse_input(filepath)
    orientation, value = instructions[0]
    folded = fold_once(points, orientation, value)
    return len(folded)


def pprint(points):
    xmax, ymax = 0, 0
    for x, y in points:
        xmax = xmax if x < xmax else x
        ymax = ymax if y < ymax else y

    result = "\n"
    for y in range(ymax + 1):
        for x in range(xmax + 1):
            if (x, y) in points:
                result += "#"
            else:
                result += "."
        result += "\n"

    return result


def part_two(filepath: pathlib.Path):
    points, instructions = parse_input(filepath)
    for instruction in instructions:
        orientation, value = instruction
        points = fold_once(points, orientation, value)
    return pprint(points)
