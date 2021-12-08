import argparse
import pathlib
from aoc.common import DayFactory


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--input-path", type=pathlib.Path, help="Path to input file."
    )
    parser.add_argument("-d", "--day", type=int, help="Day number.")
    parser.add_argument(
        "-p",
        "--part",
        type=str,
        choices=["both", "1", "2"],
        help="Problem part to solve.",
    )

    return parser.parse_args()


def main():
    args = get_args()
    if args.input_path is None:
        input_path = f"inputs/d{args.day:02d}.txt"
    else:
        input_path = args.input_path

    solutions = dict()
    if args.part in ["1", "both"]:
        solver = DayFactory.get_solver(args.day, 1)
        solutions[1] = solver(input_path)

    if args.part in ["2", "both"]:
        solver = DayFactory.get_solver(args.day, 2)
        solutions[2] = solver(input_path)

    for p, solution in solutions.items():
        print(f"Solution for day {args.day} part {p}: {solution}")


if __name__ == "__main__":
    main()
