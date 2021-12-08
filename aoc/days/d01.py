import pathlib


def parse_input(filepath: pathlib.Path):
    with open(filepath) as f:
        numbers = [int(i.rstrip()) for i in f.readlines()]

    return numbers


def part_one(filepath: pathlib.Path):

    numbers = parse_input(filepath)
    increasing = sum([numbers[i + 1] > numbers[i] for i in range(len(numbers) - 1)])

    return increasing


def part_two(filepath: pathlib.Path):

    numbers = parse_input(filepath)
    increasing = sum(
        [
            sum(numbers[i + 1 : i + 4]) > sum(numbers[i : i + 3])
            for i in range(len(numbers) - 3)
        ]
    )

    return increasing
