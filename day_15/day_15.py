with open("day_15/input.txt", "r") as myfile:
    turns = [int(x) for x in myfile.read().replace("\n", "").split(",")]

numbers = {}
last_number = 0

end = 2020

for i, number in enumerate(turns):
    numbers[number] = [i]
    last_number = number

for index in range(len(turns), end):
    if len(numbers[last_number]) < 2:
        numbers[0] = [index] + [numbers[0][0]] if 0 in numbers else [index]
        last_number = 0
    else:
        difference = numbers[last_number][0] - numbers[last_number][1]
        numbers[difference] = (
            [index] + [numbers[difference][0]]
            if difference in numbers
            else [index]
        )
        last_number = difference

print(last_number)
