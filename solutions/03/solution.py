from typing import List, Tuple
import re

def read_data(path: str) -> List[List[int]]:
    """
    Reads data from a file and returns a list of lists of integers.

    :param path: path to the file
    :return: list of lists of integers
    """
    with open(path, "r") as f:
        raw_data = f.read()
    return raw_data

def find_regex(string:str) -> List[str]:
    """
    Find all occurrences of the pattern mul(x,y) in a string.

    :param string: string to search
    :return: list of occurrences
    """
    return re.findall(r"mul\([0-9]+,[0-9]+\)", string)

def parse_mult(string:str) -> Tuple[int]:
    """
    Parse the string mul(x,y) and return the two integers x,y.
    """
    string = string.strip("mul(")
    string = string.strip(")")
    return tuple(map(int, string.split(",")))

def calculate_result(data:str) -> int:
    """
    Calculate the result of the multiplication of all occurrences of mul(x,y) in the data.
    """
    result = 0
    for match in find_regex(data):
        x, y = parse_mult(match)
        result += x * y
    return result

def find_regex_part2(string:str) -> List[str]:
    """
    Find all occurrences of the pattern do(), don't() or mul(x,y) in a string.

    :param string: string to search
    :return: list of occurrences
    """
    return re.findall(r"do\(\)|mul\([0-9]+,[0-9]+\)|don't\(\)", string)

def calculate_result_part2(data:str) -> int:
    """
    Calculate the result of the multiplication of all occurrences of mul(x,y) in the data.
    """
    result = 0
    multiply = True
    for match in find_regex_part2(data):
        if "don't()" in match:
            multiply = False
        elif "do()" in match:
            multiply = True
        elif "mul" in match and multiply:
            x, y = parse_mult(match)
            result += x * y
    return result

if __name__ == "__main__":
    data = read_data("input.txt")
    print(calculate_result(data))
    print(calculate_result_part2(data))
