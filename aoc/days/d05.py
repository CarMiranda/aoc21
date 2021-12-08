import pathlib


def parse_input(filepath: pathlib.Path):
    with open(filepath) as f:
        lines = [line.rstrip().split(" -> ") for line in f.readlines()]

    sources, dests = list(zip(*lines))

    return sources, dests


def part_one(filepath: pathlib.Path):
    sources, dests = parse_input(filepath)
    board = dict()

    for src, dst in zip(sources, dests):
        x1, y1 = list(map(int, src.split(",")))
        x2, y2 = list(map(int, dst.split(",")))
        if x1 == x2:
            # Vertical
            rng = range(y1, y2 + 1) if y1 < y2 else range(y2, y1 + 1)
            for i in rng:
                if (i, x1) in board:
                    board[(i, x1)] += 1
                else:
                    board[(i, x1)] = 1
        elif y1 == y2:
            # Horizontal
            rng = range(x1, x2 + 1) if x1 < x2 else range(x2, x1 + 1)
            for j in rng:
                if (y1, j) in board:
                    board[(y1, j)] += 1
                else:
                    board[(y1, j)] = 1

    cnt2 = 0
    for v in board.values():
        if v > 1:
            cnt2 += 1

    return cnt2


def part_two(filepath: pathlib.Path):
    sources, dests = parse_input(filepath)
    board = dict()

    for src, dst in zip(sources, dests):
        x1, y1 = list(map(int, src.split(",")))
        x2, y2 = list(map(int, dst.split(",")))
        if x1 == x2:
            # Vertical
            rng = range(y1, y2 + 1) if y1 < y2 else range(y2, y1 + 1)
            for i in rng:
                if (i, x1) in board:
                    board[(i, x1)] += 1
                else:
                    board[(i, x1)] = 1
        elif y1 == y2:
            # Horizontal
            rng = range(x1, x2 + 1) if x1 < x2 else range(x2, x1 + 1)
            for j in rng:
                if (y1, j) in board:
                    board[(y1, j)] += 1
                else:
                    board[(y1, j)] = 1
        else:
            # Diagonal
            xrng = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
            yrng = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
            for xy in zip(yrng, xrng):
                if xy in board:
                    board[xy] += 1
                else:
                    board[xy] = 1

    cnt2 = 0
    for v in board.values():
        if v > 1:
            cnt2 += 1

    return cnt2
