from typing import Sequence
import pathlib
import statistics


def parse_input(filepath: pathlib.Path):
    with open(filepath) as f:
        numbers = [int(n) for n in f.read().rstrip().split(",")]

    return numbers


def sumabs(x: Sequence[int], y: int):
    return sum(abs(xx - y) for xx in x)


def sumabsn(x: Sequence[int], y: int):
    return sum(abs(xx - y) * (abs(xx - y) + 1) // 2 for xx in x)


def part_one(filepath: pathlib.Path):

    numbers = parse_input(filepath)

    return sumabs(numbers, int(statistics.median(numbers)))


def part_two(filepath: pathlib.Path):

    numbers = parse_input(filepath)

    return min([sumabsn(numbers, n) for n in numbers])
