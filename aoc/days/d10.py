import pathlib

OPENING_CHARS = [
    "(",
    "[",
    "{",
    "<",
]

CLOSING_PAIR = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

CORRUPTION_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

COMPLETION_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def parse_input(filepath: pathlib.Path):
    with open(filepath) as f:
        entries = [entry.rstrip() for entry in f.readlines()]

    return entries


def part_one(filepath: pathlib.Path):
    entries = parse_input(filepath)

    global_score = 0

    for entry in entries:
        stack = []
        score = 0
        for char in entry:
            if char in OPENING_CHARS:
                stack.append(char)
            else:
                if char == CLOSING_PAIR[stack[-1]]:
                    stack.pop()
                else:
                    score = CORRUPTION_SCORES[char]
                    break
        if score > 0:
            global_score += score

    return global_score


def part_two(filepath: pathlib.Path):
    entries = parse_input(filepath)

    scores = []
    for entry in entries:
        stack = []
        corrupted = False
        for char in entry:
            if char in OPENING_CHARS:
                stack.append(char)
            else:
                if char == CLOSING_PAIR[stack[-1]]:
                    stack.pop()
                else:
                    corrupted = True
                    break
        score = 0
        if not corrupted and len(stack) > 0:
            for char in stack[::-1]:
                score *= 5
                score += COMPLETION_SCORES[CLOSING_PAIR[char]]
            scores.append(score)

    scores.sort()

    return scores[len(scores) // 2]
