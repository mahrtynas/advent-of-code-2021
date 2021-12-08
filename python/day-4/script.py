import numpy as np
from typing import List

def parse_input(filename):
    with open(filename, "r") as f:
        numbers = [int(x) for x in f.readline().split(",")]
        _ = f.readline()
        boards = np.array([numbers.index(int(x)) for x in f.read().split()]).reshape((-1, 5, 5))        
    return numbers, boards


def get_win_index(board: np.ndarray) -> int:
    max_r = np.max(board, axis=0)
    max_c = np.max(board, axis=1)
    return np.min([max_r, max_c])


def count_score(board: np.ndarray, at_index: int, numbers: List[int]):
    unmarked = sum(numbers[x] for x in board.flatten() if x > at_index)
    return unmarked * numbers[at_index]


def main():
    numbers, boards = parse_input("input.txt")
    boards_win_at = list(map(get_win_index, boards))
    wb = np.argmin(boards_win_at)
    print("First part result", count_score(boards[wb], min(boards_win_at), numbers))
    wb = np.argmax(boards_win_at)
    print("Second part result", count_score(boards[wb], max(boards_win_at), numbers)) 


if __name__ == "__main__":
    main()
