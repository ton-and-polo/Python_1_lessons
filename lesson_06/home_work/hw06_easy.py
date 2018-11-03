# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

# 1
print("1st part:")
import math


class triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def side_AB(self):
        length = math.sqrt((self.B[0] - self.A[0]) ** 2 + (self.B[1] - self.A[1]) ** 2)
        return length
    def side_BC(self):
        length = math.sqrt((self.C[0] - self.B[0]) ** 2 + (self.C[1] - self.B[1]) ** 2)
        return length
    def side_CA(self):
        length = math.sqrt((self.A[0] - self.C[0]) ** 2 + (self.A[1] - self.C[1]) ** 2)
        return length

    def height(self):
        p = self.perimeter() / 2 # half_perimeter
        return int((2 / self.side_CA())*(math.sqrt(p * (p-self.side_CA()) * (p-self.side_AB()) * (p-self.side_BC()))))

    def area(self):
        return int((self.side_CA() / 2) * self.height())

    def perimeter(self):
        return int(self.side_AB() + self.side_BC() + self.side_CA())





triangle_1 = triangle([2, 2], [4, 5], [6, 2])

print(triangle_1.height())
print(triangle_1.area())
print(triangle_1.perimeter())



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

