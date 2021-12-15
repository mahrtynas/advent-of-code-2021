import numpy as np
from typing import Tuple


def parse_input(filename: str) -> np.ndarray:
    with open(filename, "r") as f:
        data = np.array([[int(x) for x in line.strip()] for line in f.readlines()])
    return data

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def coord_is_in_arr(coord: Tuple[int, int], h: int, w:int) -> bool:
    return 0 <= coord[0] < h and 0 <= coord[1] < w

def create_min_risk_map(arr: np.ndarray) -> np.ndarray:
    h, w = arr.shape
    output = np.empty((h, w))
    output[:] = np.NaN
    output[0, 0] = 0
    stack = [(0, 0, 0)]
    while stack:
        stack.sort()
        v, i, j = stack.pop(0)
        for d in directions:
            ii, jj = (i + d[0], j + d[1])
            if coord_is_in_arr((ii, jj), h, w) and np.isnan(output[ii, jj]):
                acc_v = int(v + arr[ii, jj])
                output[ii, jj] = acc_v
                stack.append((acc_v, ii, jj))
    return output

def expand_map(arr: np.ndarray) -> np.ndarray:
    v_arrays = []
    for i in range(5):
        h_arrays = []
        for j in range(5):
            m = arr + i + j
            h_arrays.append(np.where(m > 9, np.mod(m, 9), m))
        v_arrays.append(np.hstack(tuple(h_arrays)))
    return np.vstack(tuple(v_arrays))
            

def main():
    inp = parse_input("input.txt")
    result = create_min_risk_map(inp)
    print("Result of the first part:", result[-1, -1])
    # second part
    mm = expand_map(inp)
    result = create_min_risk_map(mm)
    print("Result of the second part", result[-1, -1])


if __name__ == "__main__":
    main()
