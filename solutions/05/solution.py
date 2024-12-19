from typing import List, Tuple

class Rule:
    def __init__(self, string: str):
        x,y = string.split("|")
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f"{self.x} | {self.y}"

    def __repr__(self):
        return self.__str__()

    def check_list(self, data: List[int]) -> bool:
        """
        check if x comes before y in the list
        """
        if self.x not in data or self.y not in data:
            return True
        return data.index(self.x) < data.index(self.y)

    def check_rule_applies(self, data: List[int]) -> bool:
        """
        Check if the rule applies to the data.
        """
        return self.x in data and self.y in data



def get_middle_element(data: List[int]) -> int:
    """
    Get the middle element of a list of integers.
    """
    return data[len(data) // 2]


def read_data(path: str) -> Tuple[List[Rule], List[List[int]]]:
    """
    Reads data from a file and returns a list of lists of integers.

    :param path: path to the file
    :return: list of lists of integers
    """
    with open(path, "r") as f:
        raw_data = f.read()

    rules, updates = raw_data.split("\n\n")
    rules = rules.split("\n")
    updates = updates.split("\n")

    rules = [Rule(rule) for rule in rules]
    updates = [list(map(int, update.split(",")))for update in updates]
    return rules, updates


def check_all_rules(rules: List[Rule], data: List[int]) -> bool:
    """
    Check if all rules are satisfied by the data.
    """
    return all(rule.check_list(data) for rule in rules)


def solve_part_1(rules: List[Rule], updates: List[List[int]]) -> int:
    """
    Solve part 1 of the puzzle.
    """
    count = 0
    for update in updates:
        if check_all_rules(rules, update):
            count += get_middle_element(update)
    return count


def reorder_update(rules, update):
    """
    Reorder the update list according to the rules.
    """
    while not check_all_rules(rules, update):
        for rule in rules:
            x_index = update.index(rule.x)
            y_index = update.index(rule.y)
            if x_index > y_index:
                update[x_index], update[y_index] = update[y_index], update[x_index]
    return update


def solve_part_2(rules: List[Rule], updates: List[List[int]]) -> int:
    """
    Solve part 2 of the puzzle.
    """
    count = 0
    for update in updates:
        if check_all_rules(rules, update):
            continue

        rules_to_apply = [rule for rule in rules if rule.check_rule_applies(update)]
        update = reorder_update(rules_to_apply, update)
        count += get_middle_element(update)
    return count

if __name__ == "__main__":
    rules, updates = read_data("input.txt")
    print(solve_part_1(rules, updates))
    print(solve_part_2(rules, updates))
