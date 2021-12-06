import numpy as np
from typing import List, Tuple, Any


def parse_coordinates(x: List[str]) -> List[List[int]]:
    return list(map(lambda x: list(map(int, x.split(","))), x))


def parse_input(filename: str):
    with open(filename, "r") as f:
        lines = [line.split("->") for line in f.readlines()]
        content = list(map(parse_coordinates, lines)) 
    return content


def is_horizontal(x: List[List[int]]) -> bool:
    return x[0][0] == x[1][0]


def is_vertical(x: List[List[int]]) -> bool:
    return x[0][1] == x[1][1]


def is_diagonal(x: List[List[int]]) -> bool:
    return abs(x[0][0] - x[1][0]) == abs(x[0][1] - x[1][1])


def subset_vertical_horizontal(lines: List[List[List[int]]]) -> List[List[List[int]]]:
    return [x for x in lines if is_horizontal(x) or is_vertical(x)]


def subset_vhd(lines: List[List[List[int]]]) -> List[List[List[int]]]:
    return [x for x in lines if is_horizontal(x) or is_vertical(x) or is_diagonal(x)]


def get_diagonal_index(coord: np.ndarray) -> Tuple[Any, Any]:
    x_step = 1 if coord[0][0] < coord[1][0] else -1
    xx = np.arange(coord[0][0], coord[1][0] + x_step, x_step)
    y_step = 1 if coord[0][1] < coord[1][1] else -1
    yy = np.arange(coord[0][1], coord[1][1] + y_step, y_step)
    return xx, yy 



def draw_line(diagram: np.ndarray, coord: np.ndarray):
    x_min, y_min = np.min(coord, axis = 0)
    x_max, y_max = np.max(coord, axis = 0)
    if x_min == x_max or y_min == y_max:
        diagram[x_min:x_max+1, y_min:y_max+1] += 1
    else:
        xx, yy = get_diagonal_index(coord)
        diagram[xx, yy] += 1


def main():
    inp = parse_input("input.txt")
    # first part
    sub_inp = subset_vertical_horizontal(inp)
    line_coordinates = np.array(sub_inp)
    N  = np.max(line_coordinates) + 1 
    diagram = np.zeros((N, N))
    for coord in line_coordinates:
        draw_line(diagram, coord)
    result = np.sum(np.where(diagram >= 2, 1, 0))
    print("First solution: ", result)
    # second part
    sub_inp = subset_vhd(inp)
    line_coordinates = np.array(sub_inp)
    N = np.max(line_coordinates) + 1
    diagram = np.zeros((N, N))
    for coord in line_coordinates:
        draw_line(diagram, coord)
    result = np.sum(np.where(diagram >= 2, 1, 0))
    print("Second solution: ", result)

if __name__ == "__main__":
    main()
    