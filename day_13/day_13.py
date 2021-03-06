import regex
from functools import reduce

with open("day_13/input.txt", "r") as myfile:
    data = myfile.readlines()

# Part One

print(
    reduce(
        lambda x, y: x * y,
        min(
            [
                (x, x - (int(data[0]) % x))
                for x in [
                    int(x.group("number"))
                    for x in list(regex.finditer(r"(?P<number>\d+)", data[1]))
                ]
            ],
            key=lambda k: k[1],
        ),
        1,
    )
)

# Part Two

parsed_buses = [
    (int(x), i) for i, x in enumerate(data[1].rstrip().split(",")) if x != "x"
]

last_time = 0
for index in range(1, len(parsed_buses) + 1):
    interval = reduce(lambda x, y: x * y, [x[0] for x in parsed_buses[: index - 1]], 1)
    current_time = last_time
    division = 0.1
    while not division.is_integer():
        current_time += interval
        bus = parsed_buses[index - 1]
        division = (current_time + bus[1]) / bus[0]
    last_time = current_time

print(last_time)
