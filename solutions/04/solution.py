from typing import List, Tuple



class WordGrid():
    def __init__(self, data: List[str]):
        self.data = data
        self.width = len(data[0])
        self.height = len(data)

    def get_char(self, x: int, y: int) -> str:
        self._check_input(x, y)
        return self.data[y][x]

    def _check_input(self, x: int, y: int) -> bool:
        if x < 0 or y < 0:
            raise ValueError('x and y must be positive integers')
        if x >= self.width or y >= self.height:
            raise ValueError('x and y must be within the grid')
        return True

    def get_horizontal_right(self, x: int, y: int, len: int) -> str:
        word = ''
        for i in range(len):
            try:
                word += self.get_char(x + i, y)
            except:
                return None
        return word

    def get_horizontal_left(self, x: int, y: int, len: int) -> str:
        word = ''
        for i in range(len):
            try:
                word += self.get_char(x - i, y)
            except:
                return None
        return word

    def get_vertical_down(self, x: int, y: int, len: int) -> str:
        word = ''
        for i in range(len):
            try:
                word += self.get_char(x, y + i)
            except:
                return None
        return word

    def get_vertical_up(self, x: int, y: int, len: int) -> str:
        word = ''
        for i in range(len):
            try:
                word += self.get_char(x, y - i)
            except:
                return None
        return word

    def get_diagonal_down_right(self, x: int, y: int, len: int) -> str:
        word = ''
        for i in range(len):
            try:
                word += self.get_char(x + i, y + i)
            except:
                return None
        return word

    def get_diagonal_down_left(self, x: int, y: int, len: int) -> str:
        word = ''
        for i in range(len):
            try:
                word += self.get_char(x - i, y + i)
            except:
                return None
        return word

    def get_diagonal_up_right(self, x: int, y: int, len: int) -> str:
        word = ''
        for i in range(len):
            try:
                word += self.get_char(x + i, y - i)
            except:
                return None
        return word

    def get_diagonal_up_left(self, x: int, y: int, len: int) -> str:
        word = ''
        for i in range(len):
            try:
                word += self.get_char(x - i, y - i)
            except:
                return None
        return word


class WordSearch():
    def __init__(self, grid: WordGrid, word = 'XMAS'):
        self.grid = grid
        self.word = word
        self.count = 0
        self.word_length = len(self.word)

    def search(self):
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                if self.grid.get_char(x, y) == self.word[0]:
                    if self.grid.get_horizontal_right(x, y, self.word_length) == self.word:
                        self.count += 1
                    if self.grid.get_horizontal_left(x, y, self.word_length) == self.word:
                        self.count += 1
                    if self.grid.get_vertical_down(x, y, self.word_length) == self.word:
                        self.count += 1
                    if self.grid.get_vertical_up(x, y, self.word_length) == self.word:
                        self.count += 1
                    if self.grid.get_diagonal_down_right(x, y, self.word_length) == self.word:
                        self.count += 1
                    if self.grid.get_diagonal_down_left(x, y, self.word_length) == self.word:
                        self.count += 1
                    if self.grid.get_diagonal_up_right(x, y, self.word_length) == self.word:
                        self.count += 1
                    if self.grid.get_diagonal_up_left(x, y, self.word_length) == self.word:
                        self.count += 1
        return self.count

class MasSearch(WordSearch):
    def __init__(self, grid: WordGrid, word = 'MAS'):
        super().__init__(grid, word)

    def search(self):
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                if self.grid.get_char(x, y) == self.word[1]:
                    if (
                        (
                            (self.grid.get_diagonal_down_right(x-1, y-1, self.word_length) == self.word)
                            or
                            (self.grid.get_diagonal_up_left(x+1, y+1, self.word_length) == self.word)
                        )
                        and
                        (
                            (self.grid.get_diagonal_down_left(x+1, y-1, self.word_length) == self.word)
                            or
                            (self.grid.get_diagonal_up_right(x-1, y+1, self.word_length) == self.word)
                        )
                    ):
                        self.count += 1
        return self.count


def read_data(path: str) -> List[List[int]]:
    """
    Reads data from a file and returns a list of lists of integers.

    :param path: path to the file
    :return: list of lists of integers
    """
    with open(path, "r") as f:
        raw_data = f.readlines()

    data = [list(line.strip()) for line in raw_data]
    return data



if __name__ == "__main__":
    data = read_data("input.txt")
    grid = WordGrid(data)
    search = WordSearch(grid)
    print(search.search())
    mas_search = MasSearch(grid)
    print(mas_search.search())
