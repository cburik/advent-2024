"""
This module contains a clean solution to both parts of the puzzle (day 1 of Advent of Code 2024).
"""
from typing import List, Tuple


def read_data(path: str) -> Tuple[List[int], List[int]]:
    """
    Reads data from a file and returns two lists of integers.

    :param path: path to the file
    :return: two lists of integers
    """
    with open(path, "r") as f:
        data = f.readlines()

    location_ids_left = []
    location_ids_right = []

    for row in data:
        left, right = row.split()
        location_ids_left.append(int(left))
        location_ids_right.append(int(right))

    location_ids_left.sort()
    location_ids_right.sort()
    return location_ids_left, location_ids_right


def sum_of_differences(location_ids_left: List[int], location_ids_right: List[int]) -> int:
    """
    Calculate the sum of differences, solves part 1 of the puzzle.

    :param location_ids_left: list of integers, left in the input data
    :param location_ids_right: list of integers, right in the input data
    :return: sum of differences
    """
    sum_of_differences = 0
    for left, right in zip(location_ids_left, location_ids_right):
        sum_of_differences += abs(left - right)
    return sum_of_differences


def count_number_in_list(number: int, lst: List[int]) -> int:
    """
    Counts the number of occurrences of a number in a list.

    :param number: number to count
    :param lst: list of integers
    :return: number of occurrences
    """
    return sum(1 for x in lst if x == number)


def calculate_similarity_score(location_ids_left: List[int], location_ids_right: List[int]) -> int:
    """
    Calculate the similarity score, solves part 2 of the puzzle.

    :param location_ids_left: list of integers, left in the input data
    :param location_ids_right: list of integers, right in the input data
    :return: similarity score
    """
    similarity_score = 0
    for x in location_ids_left:
        count = count_number_in_list(x, location_ids_right)
        similarity_score += x * count
    return similarity_score


if __name__ == "__main__":
    location_ids_left, location_ids_right = read_data("input.txt")
    print(sum_of_differences(location_ids_left, location_ids_right))
    print(calculate_similarity_score(location_ids_left, location_ids_right))
