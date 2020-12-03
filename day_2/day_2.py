import regex

with open("day_2/input.txt", "r") as myfile:
    data = myfile.readlines()

# Part One

valid_passwords = 0

for password in data:
    match = regex.match(
        r"(?P<min>\d+)\-(?P<max>\d+)\s(?P<character>[^:]+):\s(?P<password>.+)", password
    )
    min = match.group("min")
    max = match.group("max")
    character = match.group("character")
    password = match.group("password")
    occurrences = password.count(character)
    if int(min) <= occurrences <= int(max):
        valid_passwords += 1

print(valid_passwords)

# Part Two

valid_passwords = 0

for password in data:
    match = regex.match(
        r"(?P<first>\d+)\-(?P<second>\d+)\s(?P<character>[^:]+):\s(?P<password>.+)",
        password,
    )
    first = match.group("first")
    second = match.group("second")
    character = match.group("character")
    password = match.group("password")
    first_contains = password[int(first) - 1] == character
    second_contains = password[int(second) - 1] == character
    if sum([first_contains, second_contains]) == 1:
        valid_passwords += 1

print(valid_passwords)
