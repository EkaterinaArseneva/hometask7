"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()),
вычитание (__sub__()),
умножение (__mul__()),
деление (__truediv__()).
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.

"""
class OrganicCell():
    def __init__(self, units):
        self.units = int(units)

    def __str__(self):
        return str(f'organic cell with {self.units} units')

    def __add__(self, other):
        #Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
        return OrganicCell(self.units + other.units)
    def __sub__(self, other):
        #Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
        #больше нуля, иначе выводить соответствующее сообщение.
        return OrganicCell(self.units - other.units) if self.units > other.units else 'it is not possible'
    def __mul__(self, other):
        #Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
        #ячеек этих двух клеток.
        return OrganicCell(self.units*other.units)
    def __truediv__(self, other):
        #Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
        # деление количества ячеек этих двух клеток.
        if self.units // other.units >= 1:
            return OrganicCell(self.units//other.units)
        else:
            return 'it is not possible'

    def make_order(self, lines):
        self.lines = lines
        row = ''
        for i in range(self.units // lines):
            row += '*' * lines + '\\n'
        row += '*' * (self.units % lines)
        return row



cell1 = OrganicCell(6)
cell2 = OrganicCell(22)
print(cell1 + cell2)
print(cell2 - cell1)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1/cell2)

print(cell2.make_order(5))