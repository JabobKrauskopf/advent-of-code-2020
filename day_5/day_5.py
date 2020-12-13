with open("day_5/input.txt", "r") as myfile:
    rows = [x.replace("\n", "") for x in myfile.readlines()]

seat_ids = [
    int(
        x.replace("B", "1").replace("R", "1").replace("F", "0").replace("L", "0"),
        2,
    )
    for x in rows
]

# Part One

print(max(seat_ids))

# Part Two

filtered_ids = [
    x for x in list(range(0, int("1111111111", 2) + 1)) if x not in seat_ids
]

seat_id = [
    x
    for x in [x for x in filtered_ids if x + 1 not in filtered_ids]
    if x - 1 not in filtered_ids
][0]

print(seat_id)
