with open("day_1/input.txt", "r") as myfile:
    data = [int(x) for x in myfile.readlines()]

# Part One

for element in data:
    if element < 2020:
        for second_element in data:
            if element + second_element == 2020:
                print(element * second_element)

# Part Two

for element in data:
    if element < 2020:
        for second_element in data:
            first_sum = element + second_element
            if first_sum < 2020:
                for third_element in data:
                    if first_sum + third_element == 2020:
                        print(element * second_element * third_element)
                        break
                break
