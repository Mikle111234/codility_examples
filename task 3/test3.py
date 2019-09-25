class Matrix:
    def __init__(self, A):
        self.matrix = A
        self.height = self.get_height()
        self.width = self.get_width()

    def get_height(self):
        return len(self.matrix)

    def get_width(self):
        return len(self.matrix[0])

    def get_cell_color(self, i, j):
        if i < 0 or j < 0 or i >= self.height or j >= self.width:
            return None
        return self.matrix[i][j]

    def set_cell_color(self, i, j, color):
        if i < 0 or j < 0 or i >= self.height or j >= self.width:
            return
        self.matrix[i][j] = color


def check_color(country_map, i, j, new_color, checked_color):
    if i < 0 or j < 0 or i >= country_map.height or j >= country_map.width:
        return
    cell_color = country_map.get_cell_color(i, j)
    if cell_color == checked_color:
        return
    if cell_color != new_color:
        return
    country_map.set_cell_color(i, j, checked_color)

    check_color(country_map, i,   j-1, new_color, checked_color)
    check_color(country_map, i-1, j,   new_color, checked_color)
    check_color(country_map, i,   j+1, new_color, checked_color)
    check_color(country_map, i+1, j,   new_color, checked_color)


def solution(A):
    country_map = Matrix(A)

    countries = 0
    checked_color = 'checked'

    for i in range(country_map.height):
        for j in range(country_map.width):
            country_color = country_map.get_cell_color(i, j)
            if country_color != checked_color:
                countries += 1
                check_color(country_map, i, j, country_color, checked_color)
    print(countries)
    return countries


if __name__ == '__main__':
    A = [
        [5, 4, 4],
        [4, 3, 4],
        [3, 2, 4],
        [2, 2, 2],
        [3, 3, 4],
        [1, 4, 4],
        [4, 1, 1],
    ]
    solution(A)
