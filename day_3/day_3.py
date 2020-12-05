with open("day_3/input.txt", "r") as myfile:
    data = myfile.readlines()

matrix = []

right = 3
down = 1

for row in data:
    new_row = [
        False if character == "." else True for character in row[: (len(row) - 1)]
    ]
    matrix.append(new_row)

# Part One

index = 0

encounters = 0

for i in range(0, len(matrix), down):
    if matrix[i][index]:
        encounters += 1
    index = (index + right) % len(matrix[0])

print(encounters)

# Part Two

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

product = 1

for slope in slopes:
    encounters = 0
    index = 0
    for i in range(0, len(matrix), slope[1]):
        if matrix[i][index]:
            encounters += 1
        index = (index + slope[0]) % len(matrix[0])

    product *= encounters

print(product)
