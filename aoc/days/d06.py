import pathlib


def parse_input(filepath: pathlib.Path):
    with open(filepath) as f:
        fish = list(map(int, f.read().rstrip().split(",")))

    return fish


class Fish:
    def __init__(self, initial_timer):
        self.timer = initial_timer

    def step(self):
        self.timer -= 1
        if self.timer == -1:
            self.reset()
            return True
        return False

    def reset(self):
        self.timer = 6


def part_one(filepath: pathlib.Path):

    fish = parse_input(filepath)

    fish = [Fish(i) for i in fish]

    for _ in range(80):
        new_ones = []
        for f in fish:
            if f.step():
                new_ones.append(Fish(8))
        fish.extend(new_ones)

    return len(fish)


def part_two(filepath: pathlib.Path):

    fish = parse_input(filepath)

    sfish = {i: 0 for i in set(fish)}
    for f in fish:
        sfish[f] += 1

    for _ in range(256):
        ssfish = {i - 1: v for i, v in sfish.items()}
        if -1 in ssfish:
            ssfish[8] = ssfish[-1]
            ssfish[6] = ssfish.get(6, 0) + ssfish[-1]
            del ssfish[-1]
        sfish = ssfish

    return sum(sfish.values())
