instructions = [
    {
        "executed": False,
        "command": row.split(" ")[0],
        "argument": int(row.split(" ")[1]),
    }
    for row in open("day_8/input.txt", "r").readlines()
]

# Part One


def check_instructions(instructions):
    command_counter = 0
    counter = 0
    try:
        while not instructions[command_counter]["executed"]:
            instruction = instructions[command_counter]
            instruction["executed"] = True
            if instruction["command"] == "nop":
                command_counter += 1
            elif instruction["command"] == "acc":
                counter += instruction["argument"]
                command_counter += 1
            elif instruction["command"] == "jmp":
                command_counter += instruction["argument"]
    except IndexError:
        return counter, command_counter
    return counter, command_counter


print(check_instructions([x.copy() for x in instructions])[0])

# Part Two


for index in [
    i for i in range(len(instructions)) if instructions[i]["command"] in ["nop", "jmp"]
]:
    instructions_copy = [x.copy() for x in instructions]
    instructions_copy[index]["command"] = (
        "nop" if instructions_copy[index]["command"] == "jmp" else "jmp"
    )
    counter, command_counter = check_instructions(instructions_copy)
    if command_counter >= len(instructions_copy):
        print(counter)
        break
