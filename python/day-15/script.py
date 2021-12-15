import numpy as np


def parse_input(filename):
    with open(filename, "r") as f:
        data = np.array([[int(x) for x in line.strip()] for line in f.readlines()])
    return data

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def coord_is_in_arr(coord, h, w):
    return 0 <= coord[0] < h and 0 <= coord[1] < w

def add_acc_risk(arr):
    h, w = arr.shape
    output = np.empty((h, w))
    output[:] = np.NaN
    output[0, 0] = 0
    stack = [(0, 0, 0)]
    while stack:
        stack.sort()
        v, i, j = stack.pop(0)
        for d in directions:
            p = (i + d[0], j + d[1])
            if coord_is_in_arr(p, h, w) and np.isnan(output[p[0], p[1]]):
                acc_v = v + arr[p[0], p[1]]
                output[p[0], p[1]] = acc_v
                stack.append((acc_v, p[0], p[1]))
    return output


def expand_map(arr):
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
    result = add_acc_risk(inp)
    print(result)
    # second part
    mm = expand_map(inp)
    result = add_acc_risk(mm)
    print(result)


if __name__ == "__main__":
    main()
