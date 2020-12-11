from copy import deepcopy

with open("day_11/input.txt", "r") as myfile:
    data = [[list(x.replace("\n", "")) for x in myfile.readlines()]]
    data.append(deepcopy(data[0]))

# Part One


def is_safe(index):
    if index[0] < 0 or index[1] < 0:
        return False
    try:
        data[0][index[1]][index[0]]
        return True
    except IndexError:
        return False


def check_seat(index_x, index_y):
    occupied_count = sum(
        [
            1 if data[0][x[1]][x[0]] == "#" else 0
            for x in [
                x
                for x in [
                    (index_x - 1, index_y - 1),
                    (index_x, index_y - 1),
                    (index_x + 1, index_y - 1),
                    (index_x - 1, index_y),
                    (index_x + 1, index_y),
                    (index_x - 1, index_y + 1),
                    (index_x, index_y + 1),
                    (index_x + 1, index_y + 1),
                ]
                if is_safe(x)
            ]
        ]
    )
    changes = False
    if data[0][index_y][index_x] == "L" and occupied_count == 0:
        data[1][index_y][index_x] = "#"
        changes = True
    elif data[0][index_y][index_x] == "#" and occupied_count >= 4:
        data[1][index_y][index_x] = "L"
        changes = True
    return changes


stable = False

while not stable:
    did_change = []
    for index_y in range(len(data[0])):
        for index_x in range(len(data[0][index_y])):
            did_change.append(check_seat(index_x, index_y))
    stable = not (True in did_change)
    data[0] = deepcopy(data[1])

counter2 = 0
for index_y in range(len(data[0])):
    for index_x in range(len(data[0][index_y])):
        if data[0][index_y][index_x] == "#":
            counter2 += 1

print(counter2)

# Part Two

with open("day_11/input.txt", "r") as myfile:
    data = [[list(x.replace("\n", "")) for x in myfile.readlines()]]
    data.append(deepcopy(data[0]))


def get_visible_seats(index_x, index_y):
    indices = []
    counter = 1
    while True:
        if is_safe((index_x - counter, index_y)):
            if data[0][index_y][index_x - counter] != ".":
                indices.append((index_x - counter, index_y))
                break
        else:
            break
        counter += 1
    counter = 1
    while True:
        if is_safe((index_x + counter, index_y)):
            if data[0][index_y][index_x + counter] != ".":
                indices.append((index_x + counter, index_y))
                break
        else:
            break
        counter += 1
    counter = 1
    while True:
        if is_safe((index_x - counter, index_y - counter)):
            if data[0][index_y - counter][index_x - counter] != ".":
                indices.append((index_x - counter, index_y - counter))
                break
        else:
            break
        counter += 1
    counter = 1
    while True:
        if is_safe((index_x + counter, index_y + counter)):
            if data[0][index_y + counter][index_x + counter] != ".":
                indices.append((index_x + counter, index_y + counter))
                break
        else:
            break
        counter += 1
    counter = 1
    while True:
        if is_safe((index_x + counter, index_y - counter)):
            if data[0][index_y - counter][index_x + counter] != ".":
                indices.append((index_x + counter, index_y - counter))
                break
        else:
            break
        counter += 1
    counter = 1
    while True:
        if is_safe((index_x - counter, index_y + counter)):
            if data[0][index_y + counter][index_x - counter] != ".":
                indices.append((index_x - counter, index_y + counter))
                break
        else:
            break
        counter += 1
    counter = 1
    while True:
        if is_safe((index_x, index_y - counter)):
            if data[0][index_y - counter][index_x] != ".":
                indices.append((index_x, index_y - counter))
                break
        else:
            break
        counter += 1
    counter = 1
    while True:
        if is_safe((index_x, index_y + counter)):
            if data[0][index_y + counter][index_x] != ".":
                indices.append((index_x, index_y + counter))
                break
        else:
            break
        counter += 1
    return indices


# print(get_visible_seats(3, 4))


def check_seat(index_x, index_y):
    occupied_count = sum(
        [
            1 if data[0][x[1]][x[0]] == "#" else 0
            for x in get_visible_seats(index_x, index_y)
        ]
    )
    changes = False
    if data[0][index_y][index_x] == "L" and occupied_count == 0:
        data[1][index_y][index_x] = "#"
        changes = True
    elif data[0][index_y][index_x] == "#" and occupied_count >= 5:
        data[1][index_y][index_x] = "L"
        changes = True
    return changes


stable = False

while not stable:
    did_change = []
    for index_y in range(len(data[0])):
        for index_x in range(len(data[0][index_y])):
            did_change.append(check_seat(index_x, index_y))
    stable = not (True in did_change)
    data[0] = deepcopy(data[1])

counter2 = 0
for index_y in range(len(data[0])):
    for index_x in range(len(data[0][index_y])):
        if data[0][index_y][index_x] == "#":
            counter2 += 1

print(counter2)
