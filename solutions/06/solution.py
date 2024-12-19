from typing import List, Tuple
from enum import Enum
from copy import deepcopy

OBSTACLE = "#"
FREE = "."
START = "^"

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def turn_right(self):
        return Direction((self.value + 1) % 4)

    def take_step(self, x: int, y: int) -> Tuple[int, int]:
        if self == Direction.UP:
            return x, y - 1
        elif self == Direction.RIGHT:
            return x + 1, y
        elif self == Direction.DOWN:
            return x, y + 1
        elif self == Direction.LEFT:
            return x - 1, y
        else:
            raise ValueError("Invalid direction")

class Map:
    def __init__(self, data: List[List[str]]):
        self.data = data
        self.width = len(data[0])
        self.height = len(data)
        self.current_position = self._find_start()
        self.current_direction = Direction.UP
        self.former_positions = set()
        self.former_positions_and_directions = set()
        self.log_current_position()

    def _find_start(self) -> Tuple[int, int]:
        for y, row in enumerate(self.data):
            for x, char in enumerate(row):
                if char == START:
                    return x, y
        raise ValueError("No start found")

    def log_current_position(self):
        self.former_positions.add(self.current_position)
        self.former_positions_and_directions.add((self.current_position, self.current_direction))

    def get_char(self, x: int, y: int) -> str:
        return self.data[y][x]

    def is_out_of_bounds(self, position: Tuple[int, int]) -> bool:
        x, y = position
        return x < 0 or x >= self.width or y < 0 or y >= self.height

    def next_position(self) -> Tuple[int, int]:
        x, y = self.current_position
        return self.current_direction.take_step(x, y)

    def reset(self):
        self.current_position = self._find_start()
        self.current_direction = Direction.UP
        self.former_positions = set()
        self.former_positions_and_directions = set()
        self.log_current_position()

    def add_obstacle(self, position: Tuple[int, int]):
        x, y = position
        self.data[y][x] = OBSTACLE

    def remove_obstacle(self, position: Tuple[int, int]):
        x, y = position
        self.data[y][x] = FREE


def read_data(path: str) -> List[List[str]]:
    with open(path, "r") as f:
        raw_data = f.readlines()

    data = [list(line.strip()) for line in raw_data]
    return data


def solve_part_1(map: Map) -> int:
    while True:
        possible_position = map.next_position()

        if map.is_out_of_bounds(possible_position):
            break

        if map.get_char(*possible_position) == OBSTACLE:
            map.current_direction = map.current_direction.turn_right()
            continue
        elif map.get_char(*possible_position) == FREE or map.get_char(*possible_position) == START:
            map.current_position = possible_position
            map.log_current_position()
        else:
            raise ValueError("Invalid character")

    return len(map.former_positions)


def does_it_loop(map: Map):
    while True:
        possible_position = map.next_position()
        if (possible_position, map.current_direction) in map.former_positions_and_directions:
            return True

        if map.is_out_of_bounds(possible_position):
            return False

        if map.get_char(*possible_position) == OBSTACLE:
            map.current_direction = map.current_direction.turn_right()
            continue
        elif map.get_char(*possible_position) == FREE or map.get_char(*possible_position) == START:
            map.current_position = possible_position
            map.log_current_position()
        else:
            raise ValueError("Invalid character")

def solve_part_2(map: Map) -> int:
    possible_obstacles_positions = map.former_positions

    count = 0
    map.reset()
    for i, position in enumerate(possible_obstacles_positions):
        if i % 100 == 0:
            print(f"Checking position {i}/{len(possible_obstacles_positions)}")
        map_copy = deepcopy(map)
        map_copy.add_obstacle(position)
        if does_it_loop(map_copy):
            count += 1
    return count


if __name__ == '__main__':
    data = read_data("input.txt")
    map = Map(data)
    print(solve_part_1(map))
    print(solve_part_2(map))

