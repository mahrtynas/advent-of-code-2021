from typing import List


def parse_input(filename: str) -> List[int]:
    with open(filename, "r") as f:
        data = f.read()
    return [int(x) for x in data.split(",")]


def update_state(state: List[int]) -> None:
    state.append(state.pop(0))
    state[6] += state[-1]


def state_after_days(state: List[int], days: int) -> None:
    for _ in range(days):
        update_state(state)
    print(f"There would be a toal of {sum(state)} fish after {days} days") 


def main():
    inp = parse_input("input.txt")
    
    # part 1:
    state = [inp.count(x) for x in range(9)]
    state_after_days(state=state, days=80)

    # part 2:
    state = [inp.count(x) for x in range(9)]
    state_after_days(state=state, days=256)


if __name__ == "__main__":
    main()
