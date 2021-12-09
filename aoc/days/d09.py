from typing import Tuple, Sequence
import pathlib


def parse_input(filepath: pathlib.Path):
    with open(filepath) as f:
        height_map = [list(map(int, line.rstrip())) for line in f.readlines()]

    return height_map


def basin_size(low_point: Tuple[int, int], hmap: Sequence[Sequence[int]]):

    to_explore = set([low_point])
    explored = set()
    bsize = 0

    while len(to_explore) > 0:
        tmp = set(to_explore)
        for i, j in tmp:
            # Check where the basin extends
            goes_up = i > 0 and hmap[i - 1][j] < 9
            goes_down = i < len(hmap) - 1 and hmap[i + 1][j] < 9
            goes_left = j > 0 and hmap[i][j - 1] < 9
            goes_right = j < len(hmap[0]) - 1 and hmap[i][j + 1] < 9

            # If not already explored, mark it
            if goes_up and (i - 1, j) not in explored:
                to_explore.add((i - 1, j))
            if goes_down and (i + 1, j) not in explored:
                to_explore.add((i + 1, j))
            if goes_left and (i, j - 1) not in explored:
                to_explore.add((i, j - 1))
            if goes_right and (i, j + 1) not in explored:
                to_explore.add((i, j + 1))

            # Mark as explored
            explored.add((i, j))
            to_explore.remove((i, j))
            bsize += 1

    return bsize


def part_one(filepath: pathlib.Path):
    hm = parse_input(filepath)

    lpoints = []
    for i in range(len(hm)):
        for j in range(len(hm[0])):
            v = hm[i][j]
            cond = True
            if i > 0:
                cond &= v < hm[i - 1][j]
            if cond and i < len(hm) - 1:
                cond &= v < hm[i + 1][j]
            if cond and j > 0:
                cond &= v < hm[i][j - 1]
            if cond and j < len(hm[0]) - 1:
                cond &= v < hm[i][j + 1]
            if cond:
                lpoints.append(v + 1)

    return sum(lpoints)


def part_two(filepath: pathlib.Path):
    hm = parse_input(filepath)

    basins = []
    for i in range(len(hm)):
        for j in range(len(hm[0])):
            v = hm[i][j]
            cond = True
            if i > 0:
                cond &= v < hm[i - 1][j]
            if cond and i < len(hm) - 1:
                cond &= v < hm[i + 1][j]
            if cond and j > 0:
                cond &= v < hm[i][j - 1]
            if cond and j < len(hm[0]) - 1:
                cond &= v < hm[i][j + 1]
            if cond:
                basins.append(basin_size((i, j), hm))

    basins.sort()

    return basins[-1] * basins[-2] * basins[-3]
