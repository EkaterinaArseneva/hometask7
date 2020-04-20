"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
 сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
import random

class Matrix():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.new_matrix = []
        self.new_matrix = Matrix.matrix_maker(self)

    def matrix_maker(self):
        for row in range(self.rows):
            new_row = [random.randint(1,100) for el in range(self.columns)]
            self.new_matrix.append(new_row)
        return self.new_matrix

    def __str__(self):
        matrix_print = str()
        for row in self.new_matrix:
            for el in row:
                matrix_print += ("{:4d}".format(el))
            matrix_print += '\n'
        return matrix_print



    def __add__(self, other):
        result = []
            # Matrix(max[self.rows, other.rows], max[self.columns, other.columns])
        for sublist in zip(self.new_matrix, other.new_matrix):
            temp = []
            for numbers in zip(sublist[0], sublist[1] ):
                temp.append( sum( numbers ) )
            result.append(temp)
        return result


new_m1 = Matrix(4, 5)
new_m2 = Matrix(4, 5)
print(new_m1)
print(new_m2)
new_m3 = new_m1 + new_m2

print(f'sum of 2 martrixes is: \n {new_m3}')
