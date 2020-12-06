groups = open("day_6/input.txt", "r").read().split("\n\n")
part_one = sum([len(set(group.replace("\n", ""))) for group in groups])
part_two = sum(
    [len(set.intersection(*[set(x) for x in group.strip().split("\n")])) for group in groups]
)
print(part_one, part_two)
