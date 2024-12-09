"""
This is a clean solution to the second day of Advent of Code 2024
"""
from typing import List, Tuple
from enum import Enum


class Direction(Enum):
    INCREASING = "increasing"
    DECREASING = "decreasing"


LOWER_BOUND = 1
UPPER_BOUND = 3


def read_data(path: str) -> List[List[int]]:
    """
    Reads data from a file and returns a list of lists of integers.

    :param path: path to the file
    :return: list of lists of integers
    """
    with open(path, "r") as f:
        raw_data = f.readlines()
    data = []
    for row in raw_data:
        data.append([int(x) for x in row.split()])
    return data


def get_direction(x: int, y: int) -> Direction:
    """
    Returns the direction of the change from x to y.

    :param x: first integer
    :param y: second integer
    :return: Direction
    """
    if x < y:
        return Direction.INCREASING
    elif x > y:
        return Direction.DECREASING
    else:
        return None


def is_safe_difference(x: int, y: int, lower_bound: int, upper_bound: int) -> bool:
    """
    Returns True if the difference between x and y is between lower_bound and upper_bound.

    :param x: first integer
    :param y: second integer
    :return: bool
    """
    return lower_bound <= abs(x - y) <= upper_bound


def is_safe_row(row: List[int], lower_bound: int, upper_bound: int) -> bool:
    """
    Returns True if the row is safe.

    :param row: list of integers
    :param lower_bound: lower bound for minimum difference
    :param upper_bound: upper bound for maximum difference
    :return: bool
    """
    first_number = row[0]
    direction = None
    for number in row[1:]:
        if not is_safe_difference(first_number, number, lower_bound, upper_bound):
            return False
        if direction is None:
            direction = get_direction(first_number, number)
        else:
            if direction != get_direction(first_number, number):
                return False
        first_number = number
    return True


def solve_part1(data: List[List[int]]) -> int:
    """
    Solves part 1 of the puzzle.

    :param data: list of lists of integers
    :return: solution to part 1, int
    """
    safe_rows = 0
    for row in data:
        if is_safe_row(row, LOWER_BOUND, UPPER_BOUND):
            safe_rows += 1
    return safe_rows


def remove_element(lst: List[int], index: int) -> List[int]:
    """
    Removes an element from a list at a given index.

    :param lst: list of integers
    :param index: index of the element to remove
    :return: list of integers
    """
    return lst[:index] + lst[index + 1 :]


def solve_part2(data: List[List[int]]) -> int:
    """
    Solves part 2 of the puzzle.

    :param data: list of lists of integers
    :return: solution to part 2, int
    """
    safe_rows = 0
    for row in data:
        if is_safe_row(row):
            safe_rows += 1
        else:
            for i in range(len(row)):
                new_row = remove_element(row, i)
                if is_safe_row(new_row):
                    safe_rows += 1
                    break
    return safe_rows


if __name__ == "__main__":
    path = "input.txt"
    data = read_data(path)
    print(solve_part1(data))
    print(solve_part2(data))
