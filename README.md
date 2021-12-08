# AOC 2021

Python solutions for [Advent Of Code](https://adventofcode.com/2021).

No optimizations are done and code is provided as chronologically written, i.e. part one can be slower than part two because part two needed a faster implementation to run.

To run it, save the task input into a text file, and use:
```python
python -m aoc [-i|--input I] -d|--day D -p|--part P
```
with `D` the day number (e.g. 1, 2, 3), `P` the part (`1`, `2` or `both`) and `I` the path to the input text file for that day.
If `I` is omitted, `inputs/d{D:02d}` will be used as path.
