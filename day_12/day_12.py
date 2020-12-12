import regex

with open("day_12/input.txt", "r") as myfile:
    commands = [
        {"direction": x.group("direction"), "argument": int(x.group("argument"))}
        for x in list(regex.finditer(r"(?P<direction>[^\d])(?P<argument>\d+)", myfile.read()))
    ]

# Part One

position = [0, 0]
direction = 90

for command in commands:
    if command["direction"] == "N":
        position[1] += command["argument"]
    if command["direction"] == "S":
        position[1] -= command["argument"]
    if command["direction"] == "W":
        position[0] -= command["argument"]
    if command["direction"] == "E":
        position[0] += command["argument"]
    if command["direction"] == "F":
        if direction == 0:
            position[1] += command["argument"]
        if direction == 90:
            position[0] += command["argument"]
        if direction == 180:
            position[1] -= command["argument"]
        if direction == 270:
            position[0] -= command["argument"]
    if command["direction"] == "L":
        direction = (direction - command["argument"]) % 360
    if command["direction"] == "R":
        direction = (direction + command["argument"]) % 360

print(abs(position[0]) + abs(position[1]))


# Part Two


position_ship = [0, 0]
relative_position = [10, 1]


def sin(angle):
    value = 0
    if abs(angle) == 90 :
        value = 1
    if abs(angle) == 270:
        value = -1
    return value if angle > 0 else -value


def rotate_point(p, angle):
    s = sin(angle)
    c = sin(angle + 90)

    p = [p[0] * c - p[1] * s, p[0] * s + p[1] * c]
    return p


for command in commands:
    if command["direction"] == "N":
        relative_position[1] += command["argument"]
    if command["direction"] == "S":
        relative_position[1] -= command["argument"]
    if command["direction"] == "W":
        relative_position[0] -= command["argument"]
    if command["direction"] == "E":
        relative_position[0] += command["argument"]
    if command["direction"] == "F":
        position_ship[0] += relative_position[0] * command["argument"]
        position_ship[1] += relative_position[1] * command["argument"]
    if command["direction"] == "L":
        relative_position = rotate_point(relative_position, command["argument"])
    if command["direction"] == "R":
        relative_position = rotate_point(relative_position, -command["argument"])

print(abs(position_ship[0]) + abs(position_ship[1]))
