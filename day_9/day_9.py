with open("day_9/input.txt", "r") as myfile:
    data = [int(x) for x in myfile.readlines()]

# Part One

lookback = 25


def check_for_sum(arr, sum):
    for index in range(len(arr)):
        for index2 in range(len(arr)):
            if index != index2:
                if arr[index] + arr[index2] == sum:
                    return True
    return False


look_for = 0

for index in range(lookback, len(data)):
    if not check_for_sum(data[index - lookback : index], data[index]):
        print(data[index])
        look_for = data[index]
        break

# Part Two

for index in range(len(data)):
    sum = 0
    counter = 0
    while sum < look_for:
        sum += data[index + counter]
        counter += 1
    if sum == look_for:
        arr = data[index : index + counter - 1]
        print(min(arr) + max(arr))
        break
