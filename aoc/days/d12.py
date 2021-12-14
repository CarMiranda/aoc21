import pathlib
from typing import Dict, Set


def parse_input(filepath: pathlib.Path):
    with open(filepath) as f:
        edges = set(tuple(edge.rstrip().split("-")) for edge in f.readlines())

    vertices = set()
    graph = dict()
    small = set()
    for edge in edges:
        if edge[0].islower():
            small.add(edge[0])
        if edge[1].islower():
            small.add(edge[1])
        vertices.add(edge[0])
        vertices.add(edge[1])
        if edge[0] not in graph:
            graph[edge[0]] = {edge[1]}
        else:
            graph[edge[0]].add(edge[1])
        if edge[1] not in graph:
            graph[edge[1]] = {edge[0]}
        else:
            graph[edge[1]].add(edge[0])

    return graph, small, vertices


def find_paths(
    graph: Dict[str, Set[str]], src: str, dst: str, explored: Set[str], small: Set[str]
):
    cnt = 0
    if src == dst:
        return 1

    if src in small:
        explored = set(explored)
        explored.add(src)

    if graph[src].issubset(explored):
        return 0

    for v in graph[src]:
        if v not in explored:
            cnt += find_paths(graph, v, dst, explored, small)
    return cnt


def find_paths2(
    graph: Dict[str, Set[str]],
    src: str,
    dst: str,
    explored: Dict[str, int],
    small: Set[str],
):
    cnt = 0
    if src == dst:
        return 1

    if src in small:
        explored = dict(explored)
        explored[src] += 1

    can_repeat = not any([cnt == 2 for cnt in explored.values()])
    all_explored = all([e in small and explored[e] >= 1 for e in graph[src]])

    if not can_repeat and all_explored:
        return 0

    for v in graph[src]:
        unexplored = explored[v] == 0
        if unexplored or can_repeat:
            cnt += find_paths2(graph, v, dst, explored, small)
    return cnt


def part_one(filepath: pathlib.Path):
    graph, small, vertices = parse_input(filepath)
    return find_paths(graph, "start", "end", set(), small)


def part_two(filepath: pathlib.Path):
    graph, small, vertices = parse_input(filepath)
    explored = {v: 0 for v in vertices}
    for s in graph["start"]:
        graph[s].remove("start")

    return find_paths2(graph, "start", "end", explored, small)
