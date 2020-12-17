from copy import deepcopy

# Part One


def is_safe(index, seats):
    if index[0] < 0 or index[1] < 0:
        return False
    try:
        seats[index[1]][index[0]]
        return True
    except IndexError:
        return False


def occupied_count_part_one(index_x, index_y, seats):
    return sum(
        [
            1 if seats[0][x[1]][x[0]] == "#" else 0
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
                if is_safe(x, seats[0])
            ]
        ]
    )


# Part Two


def get_visible_seats(index_x, index_y, seats):
    indices = []
    index_multiplier = [
        (-1, 0),
        (1, 0),
        (-1, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (0, -1),
        (0, 1),
    ]
    for multiplier in index_multiplier:
        counter = 1
        while True:
            if is_safe(
                (
                    index_x + (counter * multiplier[0]),
                    index_y + (counter * multiplier[1]),
                ),
                seats,
            ):
                if (
                    seats[index_y + (counter * multiplier[1])][
                        index_x + (counter * multiplier[0])
                    ]
                    != "."
                ):
                    indices.append(
                        (
                            index_x + (counter * multiplier[0]),
                            index_y + (counter * multiplier[1]),
                        )
                    )
                    break
            else:
                break
            counter += 1
    return indices


def occupied_count_part_two(index_x, index_y, seats):
    return sum(
        [
            1 if seats[0][x[1]][x[0]] == "#" else 0
            for x in get_visible_seats(index_x, index_y, seats[0])
        ]
    )


def simulate_seats_general(
    index_x, index_y, seats, occupied_count, occupied_count_limit
):
    seats[1][index_y][index_x] = (
        "#"
        if seats[0][index_y][index_x] == "L" and occupied_count == 0
        else (
            "L"
            if seats[0][index_y][index_x] == "#"
            and occupied_count >= occupied_count_limit
            else seats[1][index_y][index_x]
        )
    )
    return seats[1][index_y][index_x] != seats[0][index_y][index_x]


def simulate(function, data, occupied_count_limit):
    data = [data, deepcopy(data)]
    did_change = 1
    while did_change > 0:
        did_change = sum(
            [
                simulate_seats_general(
                    index_x,
                    index_y,
                    data,
                    function(index_x, index_y, data),
                    occupied_count_limit,
                )
                for index_y in range(len(data[0]))
                for index_x in range(len(data[0][index_y]))
            ]
        )
        data[0] = deepcopy(data[1])

    return sum(
        [
            1
            for index_y in range(len(data[0]))
            for index_x in range(len(data[0][index_y]))
            if data[0][index_y][index_x] == "#"
        ]
    )


print(
    simulate(
        occupied_count_part_one,
        [list(x.replace("\n", "")) for x in open("day_11/input.txt", "r").readlines()],
        4,
    ),
    simulate(
        occupied_count_part_two,
        [list(x.replace("\n", "")) for x in open("day_11/input.txt", "r").readlines()],
        5,
    ),
)
