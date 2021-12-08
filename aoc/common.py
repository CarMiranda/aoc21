import importlib


class DayFactory:
    @staticmethod
    def get_solver(day: int, part: int):
        module_name = f"aoc.days.d{day:02d}"
        day_module = importlib.import_module(module_name)
        if part == 1:
            return day_module.part_one
        elif part == 2:
            return day_module.part_two
        else:
            raise ValueError("`part` must be one of 1 or 2. Received {part}.")
