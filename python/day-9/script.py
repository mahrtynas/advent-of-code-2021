import numpy as np
from typing import List, Tuple, Set


def parse_input(filename):
    with open(filename, "r") as f:
        return np.array([[int(x) for x in list(line.strip())] for line in f.readlines()])


def pad_map(arr: np.ndarray, with_value: int) -> np.ndarray:
    return np.pad(arr, 1, constant_values=with_value)


def is_lowest(a: np.ndarray, i: int, j: int) -> bool:
    return a[i, j] < a[i-1, j] and a[i, j] < a[i+1, j] and a[i, j] < a[i, j-1] and a[i, j] < a[i, j+1]


def find_low_points(arr: np.ndarray) -> Tuple[List[Tuple[int, int]], List[int]]:
    h, w = arr.shape
    coords = []
    for i in range(1, h):
        for j in range(1, w):
            if is_lowest(arr, i, j):
                coords.append((i, j))
    return coords, [arr[i, j] for i, j in coords]


def lookup_basin(arr: np.ndarray, low_point: Tuple[int, int], basin: Set[Tuple[int, int]]):
    basin.add(low_point)
    i, j = low_point
    for d in [[i, j-1], [i-1, j], [i+1, j], [i, j+1]]:
        if 9 > arr[d[0], d[1]] > arr[i, j]:
            lookup_basin(arr, low_point=(d[0], d[1]), basin=basin)
    return basin


def main():
    inp = parse_input("input.txt")
    pmap = pad_map(inp, with_value=12)
    low_coords, low_points = find_low_points(pmap)
    print("First task result:", sum(low_points) + len(low_points))
    basin_sizes = []
    for lc in low_coords:
        basin = lookup_basin(pmap, lc, basin=set())
        basin_sizes.append(len(basin))
    basin_sizes.sort(reverse=True)
    print("Second task result:", np.product(basin_sizes[:3]))


if __name__ == "__main__":
    main()
