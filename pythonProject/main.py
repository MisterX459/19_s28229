import math

#Task 1
square = [x**2 for x in range(1, 11)]
print("List of squares of numbers:")
print(square)

#Task 2
def generate_square2(start, end):

    square2 = [x**2 for x in range(start, end+1)]
    return square2
start = 1
end = 10
square2_list = generate_square2(start, end)

print(f"List of squares of numbers from {start} to {end}:")
print(square2_list)

#task 3

class SquareGenerator:
    def generate_squares(self, start, end):
        square3 = [x**2 for x in range(start, end+1)]
        return square3
square_generator = SquareGenerator()
start = 1
end = 10
squares_list = square_generator.generate_squares(start, end)

print(f"List of squares of numbers from {start} to {end}:")
print(squares_list)

#task 4


class SquareGenerator:
    def generate_squares(self, start, end):
        square3 = [x**2 for x in range(start, end+1)]
        return square3

    def calculate_square_roots(self, numbers):

        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots


square_gen = SquareGenerator()
start = 1
end = 10
squares_list = square_gen.generate_squares(start, end)
square_roots_list = square_gen.calculate_square_roots(squares_list)

print("List of square roots of numbers from {start} to {end}:")
print(square_roots_list)

#task 5
class SquareGenerator:
    def generate_squares(self, start, end):
        square3 = [x**2 for x in range(start, end+1)]
        return square3

    def calculate_square_roots(self, numbers):

        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots


square_gen = SquareGenerator()
start = 0
end = 11

try:
    squares_list = square_gen.generate_squares(start, end)
    square_roots_list = square_gen.calculate_square_roots(squares_list)

    print("List of square roots of numbers from {start} to {end}:")
    print(square_roots_list)
except ValueError as e:
    print("Error:", e)
#task 7

from square_generator.square_generator import SquareGenerator

class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        cubes = [x**3 for x in range(start, end+1)]
        return cubes
cubic_gen = CubicGenerator()
start = 1
end = 10
cubes_list = cubic_gen.generate_cubes(start, end)
print("List of cubes of numbers from {start} to {end}:")
print(cubes_list)

#task 9

from square_generator.square_generator import SquareGenerator
class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if start >= end:
            raise ValueError("Start of the range must be less than the end.")

        square9 = [x ** 2 for x in range(start, end + 1)]
        return square9

    def generate_cubes(self, start, end):
        cubes = [x ** 3 for x in range(start, end + 1)]
        return cubes

cubic_generator = CubicGenerator()
start = 1
end = 10

try:
    squares_list = cubic_generator.generate_squares(start, end)
    print(f"List of squares of numbers from {start} to {end}:")
    print(squares_list)
except ValueError as e:
    print("Error:", e)

cubes_list = cubic_gen.generate_cubes(start, end)
print(f"List of cubes of numbers from {start} to {end}:")
print(cubes_list)

#task 10

from abc import ABC, abstractmethod
class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass
    def calculate_square_roots(self, numbers):
        square_roots = [math.sqrt(num) for num in numbers]
        return square_roots
class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):

        if start >= end:
            raise ValueError("Start of the range must be less than the end.")

        squares = [x ** 2 for x in range(start, end + 1)]
        return squares

    def generate_cubes(self, start, end):
        cubes = [x ** 3 for x in range(start, end + 1)]
        return cubes



cubic_gen = CubicGenerator()
start = 1
end = 10

try:
    squares_list = cubic_gen.generate_squares(start, end)
    print("List of squares of numbers from {start} to {end}:")
    print(squares_list)
except ValueError as e:
    print("Error:", e)

cubes_list = cubic_gen.generate_cubes(start, end)
print("List of cubes of numbers from {start} to {end}:")
print(cubes_list)
