"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
 Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
 К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
 размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Cloths():
    def __init__(self,):
        self.cloths = []

    def add_cloths(self, new_object):
        self.cloths.append(new_object)

    def total_material_count(self):
        total_material = 0
        for el in self.cloths:
            total_material += el.material
        return total_material

class Coat(Cloths):
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.material = self.size / 6.5 + 0.5

    @property
    def size(self):
        return int(self.__size)

    @size.setter
    def size(self, size):
        if size < 36:
            self.__size = 36
        elif size > 52:
            self.__size = 52
        else:
            self.__size = size


class Suit(Cloths):
    def __init__(self, name, height):
        self.name = name
        self.height = height
        self.material = 2 * self.height + 0.3

    @property
    def height(self):
        return int(self.__height)

    @height.setter
    def height(self, height):
        if height < 1.5:
            self.__height = 1.5
        elif height > 2.2:
            self.__height = 2.2
        else:
            self.__height = height


cloth = Cloths()
my_coat = Coat('my_coat', 30)
my_suit = Suit('my_suit', 6)
cloth.add_cloths(my_coat)
cloth.add_cloths(my_suit)

materials = cloth.total_material_count()

for el in cloth.cloths:
    print(f'name: {el.name}, size or hight: {el.size if type(el) is Coat else el.height}, needed material: {el.material}')
print(f'total materials needed: {materials}')
