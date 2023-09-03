"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода.
Например, нельзя создавать прямоугольник со сторонами отрицательной длины.
"""

# Решение взято ваше. Разбор посмотрел.

class NegativeWidthError(ValueError):
    def __init__(self, value):
        self.value = value
        self.message = f"Invalid width: {value}. Width cannot be negative."

class NegativeHeightError(ValueError):
    def __init__(self, value):
        self.value = value
        self.message = f"Invalid height: {value}. Height cannot be negative."

class Rectangle:
    def __init__(self, width, height):
        self._width = None
        self._height = None
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise NegativeWidthError(value)
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise NegativeHeightError(value)
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)


rectangle = Rectangle(4, 5)
print("Width:", rectangle.width)
print("Height:", rectangle.height)
print("Area:", rectangle.area)
print("Perimeter:", rectangle.perimeter)

rectangle.width = 6
rectangle.height = 8
print("Updated Width:", rectangle.width)
print("Updated Height:", rectangle.height)
print("Updated Area:", rectangle.area)
print("Updated Perimeter:", rectangle.perimeter)

try:
    rectangle.width = -2
except NegativeWidthError as e:
    print("Error:", e.message)

try:
    rectangle.height = -3
except NegativeHeightError as e:
    print("Error:", e.message)