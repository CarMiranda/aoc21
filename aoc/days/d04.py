import pathlib


def parse_input(filepath: pathlib.Path):
    with open(filepath) as f:
        chunks = f.read().rstrip().split("\n\n")

    numbers, boards = chunks[0], chunks[1:]

    parsed_numbers = list(map(int, numbers.split(",")))

    parsed_boards = []
    for board in boards:
        b = [
            list(
                map(
                    int,
                    [c0 + c1 if c0 != " " else c1 for c0, c1 in zip(ll[::3], ll[1::3])],
                )
            )
            for ll in board.split("\n")
        ]
        parsed_boards.append(BingoBoard(b))

    return parsed_numbers, parsed_boards


class BingoBoard:
    def __init__(self, lines):
        self.lines = lines
        self.marked = [[False for _ in list(zip(*lines))] for _ in lines]

    def mark(self, n):
        for i, line in enumerate(self.lines):
            for j, value in enumerate(line):
                if value == n:
                    self.marked[i][j] = True

    def has_bingo(self):
        return self._check_lines() or self._check_columns()

    def _check_lines(self):
        for i, line in enumerate(self.marked):
            if sum(line) == len(line):
                return True
        return False

    def _check_columns(self):
        for j, column in enumerate(list(zip(*self.marked))):
            if sum(column) == len(column):
                return True
        return False

    def sum_unmarked(self):
        acc = 0
        for vline, mline in zip(self.lines, self.marked):
            for value, marked in zip(vline, mline):
                acc += value * (1 - marked)

        return acc


def part_one(filepath: pathlib.Path):
    numbers, boards = parse_input(filepath)

    for n in numbers:
        for b in boards:
            b.mark(n)
            has_won = b.has_bingo()
            if has_won:
                return b.sum_unmarked() * n


def part_two(filepath: pathlib.Path):
    numbers, boards = parse_input(filepath)

    latest = None
    have_won = [False] * len(boards)
    for n in numbers:
        for i, b in enumerate(boards):
            if have_won[i]:
                continue
            b.mark(n)
            if b.has_bingo():
                latest = b
                have_won[i] = True
        if all(have_won):
            break

    return latest.sum_unmarked() * n
