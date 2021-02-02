# 1
class Matrix:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.list_of_list)

    def __add__(self, other):
        summ_matix = [[a + b for a, b in zip(i, j)] for i, j in zip(self.list_of_list, other.list_of_list)]
        return Matrix(summ_matix)


matrix_1 = Matrix([[1,2,3],[1,3,2],[2,3,1]])
matrix_2 = Matrix([[4,5,6],[5,4,6],[6,5,4]])
matrix_3 = Matrix([[1,1,1],[2,2,2],[3,3,3]])
print(matrix_1)
print(matrix_2)
print(matrix_3)
print(matrix_1+matrix_2+matrix_3)