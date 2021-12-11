import pathlib


def parse_input(filepath: pathlib.Path):
    with open(filepath) as f:
        octopuses = [list(map(int, entry.rstrip())) for entry in f.readlines()]

    return octopuses


def pprint(octo):
    for line in octo:
        print("".join(map(str, line)))
    print("")


def part_one(filepath: pathlib.Path):
    octopuses = parse_input(filepath)

    n_flashes = 0
    # pprint(octopuses)

    for _ in range(100):
        # Natural increase
        octo = [[(o + 1) % 10 for o in line] for line in octopuses]
        flashed = {(i, j) for i in range(10) for j in range(10) if octo[i][j] == 0}
        already_flashed = set(flashed)

        # Flash synergy
        while len(flashed) > 0:
            tmp = set(flashed)
            flashed = set()
            for i, j in tmp:
                yrng = range(max(0, i - 1), min(10, i + 2))
                xrng = range(max(0, j - 1), min(10, j + 2))
                for ii in yrng:
                    for jj in xrng:
                        if (
                            not (ii == i and jj == j)
                            and (ii, jj) not in already_flashed
                        ):
                            octo[ii][jj] = (octo[ii][jj] + 1) % 10
                            if octo[ii][jj] == 0:
                                flashed.add((ii, jj))
                                already_flashed.add((ii, jj))
        n_flashes += len(already_flashed)
        octopuses = octo
        # pprint(octopuses)

    return n_flashes


def part_two(filepath: pathlib.Path):
    octopuses = parse_input(filepath)

    n_flashes = 0
    step = 0
    # pprint(octopuses)

    while sum(sum(line) for line in octopuses) > 0:
        # Natural increase
        octo = [[(o + 1) % 10 for o in line] for line in octopuses]
        flashed = {(i, j) for i in range(10) for j in range(10) if octo[i][j] == 0}
        already_flashed = set(flashed)

        # Flash synergy
        while len(flashed) > 0:
            tmp = set(flashed)
            flashed = set()
            for i, j in tmp:
                yrng = range(max(0, i - 1), min(10, i + 2))
                xrng = range(max(0, j - 1), min(10, j + 2))
                for ii in yrng:
                    for jj in xrng:
                        if (
                            not (ii == i and jj == j)
                            and (ii, jj) not in already_flashed
                        ):
                            octo[ii][jj] = (octo[ii][jj] + 1) % 10
                            if octo[ii][jj] == 0:
                                flashed.add((ii, jj))
                                already_flashed.add((ii, jj))
        n_flashes += len(already_flashed)
        octopuses = octo
        step += 1
        # pprint(octopuses)

    return step
