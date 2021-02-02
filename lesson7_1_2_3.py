# 1
class Matrix:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.list_of_list)

    def __add__(self, other):
        summ_matix = [[a + b for a, b in zip(i, j)] for i, j in zip(self.list_of_list, other.list_of_list)]





matrix_1 = Matrix([[1,2,3],[1,3,2],[2,3,1]])
matrix_2 = Matrix([[4,5,6],[5,4,6],[6,5,4]])
matrix_3 = Matrix([[1,1,1],[2,2,2],[3,3,3]])
print(matrix_1)
print(matrix_2)
print(matrix_3)
print(matrix_1+matrix_2+matrix_3)

# 3

class Cell:

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return self.quantity * "*"

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        delta = self.quantity - other.quantity
        if delta < 0:
            raise ValueError('Операция не может быть выполнена.')
        return Cell(delta)

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(round(self.quantity / other.quantity))

    def make_order(self, cells_by_row):
        row = ''
        for i in range(int(self.quantity / cells_by_row)):
            row += f'{"*" * cells_by_row}\\n'
        row += f'{"*" * (self.quantity % cells_by_row)}'
        return row


organic_cells_1 = Cell(10)
organic_cells_2 = Cell(7)
print(organic_cells_1)
print(organic_cells_2)
print(organic_cells_1+organic_cells_2)
print(organic_cells_1-organic_cells_2)
print(organic_cells_1*organic_cells_2)
print(organic_cells_1/organic_cells_2)
print(organic_cells_1.make_order(4))
print(organic_cells_2.make_order(5))