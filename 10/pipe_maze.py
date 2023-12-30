#!/usr/bin/python3
from operator import add

from .dijkstra import DijkstraSPF

# method
# we need to parse the graph which seems the most complicated part
# then apply a shorter path algorithm which would be dijkstra. We can use a std lib algo
# or implement it ourselves. I will implement it myself for the fun of it and the sweet
# sweet memories of telecom algo classes

# all nodes will be represented with their x,y position in the maze as a tuple of int
# the maze will be a dict which is faster to search in than a list

# to analyse connexions we need to determine orientations of the pipes, we will associates
# orientations to a pipe symbole then determine if other symbols around are compatibles

# strat: generate an oriented graph as dict from every item in the maze
# then purge all non bidirectional edges
# then apply dijkstra to find the shortest path

# x,y movment to follow direction
orientations: dict[str, tuple[int, int]] = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
}
pipes: dict[str, list[str]] = {
    "-": ["E", "W"],
    "|": ["N", "S"],
    "7": ["S", "W"],
    "F": ["E", "S"],
    "J": ["N", "W"],
    "L": ["E", "N"],
    ".": [],
    "S": ["N", "E", "S", "W"],
}


def get_oriented_edges(
    pipe_type: str, position: tuple[int, int]
) -> list[tuple[int, int]]:
    return [
        tuple(map(add, position, orientations[direction]))
        for direction in pipes[pipe_type]
    ]


def purge_non_bidirectional_edges(graph: dict) -> dict:
    """Return a graph with only bidirectional edges"""
    for node in graph:
        for edge in graph[node]:
            if edge not in graph:
                continue  # drop non existing edges like negative positions
            if node not in graph[edge]:
                graph[node].pop(edge)
    return {}


def build_oriented_graph(maze: list[list[str]]) -> dict:
    graph = {}
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            graph[(x, y)] = get_oriented_edges(maze[y][x], (x, y))

    return graph


def get_start(data: list[list[str]]) -> tuple[int, int]:
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "S":
                return (x, y)
    return (0, 0)


def build_graph(data: list[list[str]]) -> dict:
    return purge_non_bidirectional_edges(build_oriented_graph(data))


def parse_data(data: str) -> list[list[str]]:
    return [list(line) for line in data.splitlines()]


def dijkstra(graph: dict, start: tuple[int, int]) -> DijkstraSPF:
    """Return the shortest path between start and end in graph"""
    return DijkstraSPF(graph, start)


def get_further_point() -> tuple[int, int]:
    # return dijkstra.get_distance(end)
    return (0, 0)


def solve_part_1(data: list[list[str]]) -> int:
    graph = build_graph(data)
    start = get_start(data)

    dijkstra(graph, start)
    return 0


def main(file: str):
    with open(file, "r") as f:
        data = f.read()

    parsed = parse_data(data)
    result = solve_part_1(parsed)

    # print(f"Result 1: {result}")


if __name__ == "__main__":
    main("10/input.txt")
