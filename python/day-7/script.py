from typing import Callable, List
from functools import reduce
import numpy as np

def parse_input(filename):
    with open(filename, "r") as f:
        content = [int(x) for x in f.readline().split(",")]
    return content

def calculate_cost(positions: List[int], align_position: int) -> int:
    return sum([abs(x - align_position) for x in positions])

def aesum(x) -> int:
    x = abs(x)
    return int(x * (x + 1) / 2)


def calculate_actual_cost(positions: List[int], align_position: int) -> int:
    return sum([aesum(x - align_position) for x in positions])


def find_cheapest(positions: List[int], func: Callable) -> int:
    x_min = min(positions)
    x_max = max(positions)
    cost = aesum(x_max) * len(positions)
    for i in range(x_min, x_max):
        cost = min(cost, func(positions, i))
    return cost
    
def main():
    positions = parse_input("input.txt")
    print(np.median(positions))
    print(np.mean(positions))
    cheapest = find_cheapest(positions, calculate_cost)
    print(cheapest)
    # part 2:
    cheapest = find_cheapest(positions, calculate_actual_cost)
    print(cheapest)



if __name__ == "__main__":
    main()
