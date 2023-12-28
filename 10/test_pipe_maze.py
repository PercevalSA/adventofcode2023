#!/usr/bin/python3
import pipe_maze


def test_oriented_edges():
    assert pipe_maze.get_oriented_edges("F", (0, 0)) == [(1, 0), (0, 1)]
    assert pipe_maze.get_oriented_edges("7", (0, 0)) == [(0, 1), (-1, 0)]
    assert pipe_maze.get_oriented_edges("-", (0, 0)) == [(1, 0), (-1, 0)]
    assert pipe_maze.get_oriented_edges("|", (0, 0)) == [(0, -1), (0, 1)]
    assert pipe_maze.get_oriented_edges("J", (0, 0)) == [(0, -1), (-1, 0)]
    assert pipe_maze.get_oriented_edges("L", (0, 0)) == [(1, 0), (0, -1)]
    assert pipe_maze.get_oriented_edges("F", (1, 1)) == [(2, 1), (1, 2)]
