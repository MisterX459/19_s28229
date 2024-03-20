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

