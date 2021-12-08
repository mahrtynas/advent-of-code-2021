from typing import List, Dict, Set, Tuple
from pprint import pprint

def parse_input(filename):
    with open(filename, "r") as f:
        content = [[[s.strip() for s in x.strip().split(" ")] for x in line.split("|")] for line in f.readlines()]
        return content

MAP = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
}

def count_output_1478(signals: List[List[List[str]]]) -> int:
    return sum(1 for line in signals for x in line[1] if len(x) in (2, 3, 4, 7))


def find_9(signal: List[str], decoded: Dict[int, Set]) -> Tuple[List[str], Dict[int, Set]]:
    i = 0
    while set(signal[i]).intersection(decoded[4]) != decoded[4]:
        i += 1
    decoded[9] = set(signal.pop(i))
    return signal, decoded

def find_5(signal: List[str], decoded: Dict[int, Set]) -> Tuple[List[str], Dict[int, Set]]:
    i = 0
    while set(signal[i]).union(decoded[1]) != decoded[9]:
        i += 1
    decoded[5] = set(signal.pop(i))
    return signal, decoded


def find_0(signal: List[str], decoded: Dict[int, Set]) -> Tuple[List[str], Dict[int, Set]]:
    i = 0
    while len(signal[i]) != 6 or set(signal[i]).intersection(decoded[7]) != decoded[7]:
        i += 1
    decoded[0] = set(signal.pop(i))
    return signal, decoded

def find_6(signal: List[str], decoded: Dict[int, Set]) -> Tuple[List[str], Dict[int, Set]]:
    i = 0
    while len(signal[i]) != 6:
        i += 1
    decoded[6] = set(signal.pop(i))
    return signal, decoded

def find_3(signal: List[str], decoded: Dict[int, Set]) -> Tuple[List[str], Dict[int, Set]]:
    i = 0
    while set(signal[i]).intersection(decoded[7]) != decoded[7]:
        i += 1
    decoded[3] = set(signal.pop(i))
    return signal, decoded

def decode_signal(signal: List[str]) -> Dict[int, Set]:
    decoded = {MAP.get(len(x)): set(x) for x in signal if len(x) in (2, 3, 4, 7)}
    signal = [set(x) for x in signal if len(x) not in (2, 3, 4, 7)]
    signal, decoded = find_9(signal, decoded)
    signal, decoded = find_5(signal, decoded)
    signal, decoded = find_0(signal, decoded)
    signal, decoded = find_6(signal, decoded)
    signal, decoded = find_3(signal, decoded)
    decoded[2] = set(signal[0])
    return decoded


def decode_value(value: str, encryption: Dict[int, Set]) -> int:
    for k, v in encryption.items():
        if v == set(value):
            return k 


def decode_output(values: List[str], encryption: Dict[int, Set]):
    numbers = []
    for v in values:
        numbers.append(decode_value(v, encryption))
    return int("".join([str(x) for x in numbers]))


def main():
    inp = parse_input("input.txt")
    result = count_output_1478(inp)
    print("First part result: ", result)
    result = 0
    for line in inp:
        encryption = decode_signal(line[0])
        result += decode_output(line[1], encryption)
    print("Second part result: ", result)


if __name__ == "__main__":
    main()