import regex

with open("day_14/input.txt", "r") as myfile:
    data = myfile.readlines()

bits = 36

# Part One


def apply_mask_part_one(mask, number):
    binary_representation = list(bin(number)[2:])
    binary_representation = ["0"] * (
        bits - len(binary_representation)
    ) + binary_representation
    for bit in range(len(mask) - 1, -1, -1):
        if mask[bit] != "X":
            binary_representation[bit] = mask[bit]
    return int("".join(binary_representation), 2)


mem = {}
mask = ""

for line in data:
    if "mask" in line:
        mask = regex.match(r"mask = (?P<mask>.*)", line).group("mask")
    else:
        match = regex.match(r"mem\[(?P<address>\d+)\] = (?P<number>\d+)", line)
        mem[match.group("address")] = apply_mask_part_one(
            mask, int(match.group("number"))
        )

print(sum(mem.values()))


# Part Two


def apply_mask_part_one(memory, address, number, mask):
    binary_representation = list(bin(address)[2:])
    binary_representation = ["0"] * (
        bits - len(binary_representation)
    ) + binary_representation
    for bit in range(len(mask) - 1, -1, -1):
        if mask[bit] != "0":
            binary_representation[bit] = mask[bit]
    x_indices = [
        i for i in range(len(binary_representation)) if binary_representation[i] == "X"
    ]
    for i in range(2 ** len(x_indices)):
        for index in range(len(x_indices)):
            binary_representation[x_indices[index]] = (
                binary_representation[x_indices[index]]
                if i % (2 ** index) != 0
                else ("1" if binary_representation[x_indices[index]] == "0" else "0")
            )
        memory[int("".join(binary_representation), 2)] = number
    return memory


mem = {}
mask = ""

for line in data:
    if "mask" in line:
        mask = regex.match(r"mask = (?P<mask>.*)", line).group("mask")
    else:
        match = regex.match(r"mem\[(?P<address>\d+)\] = (?P<number>\d+)", line)
        mem = apply_mask_part_one(
            mem, int(match.group("address")), int(match.group("number")), mask
        )

print(sum(mem.values()))
