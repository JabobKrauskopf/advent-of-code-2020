with open("day_10/input.txt", "r") as myfile:
    data = [int(x) for x in myfile.readlines()]

data.append(max(data) + 3)
data.append(0)
sorted_data = sorted(data)

# Part One

difference = [0, 0, 0]

for index in range(len(sorted_data) - 1):
    diff = sorted_data[index + 1] - sorted_data[index] - 1
    difference[diff] += 1

print(difference[0] * difference[2])

# Part Two

cache = [-1 for x in range(len(sorted_data))]


def check_possibilities(index):
    possibilities = 0
    if index == len(sorted_data) - 1:
        return 1
    else:
        base = sorted_data[index]
        for index2 in range(3):
            try:
                if abs(sorted_data[index+index2+1] - base) <= 3:
                    if (cache[index+index2+1] == -1):
                        value = check_possibilities(index+index2+1)
                        cache[index+index2+1] = value
                    possibilities += cache[index+index2+1]
            except IndexError:
                pass
    return possibilities


print(check_possibilities(0))
