import regex

with open("day_4/input.txt", "r") as myfile:
    data = myfile.read()

passports_raw = regex.finditer(r"(?P<passport>(?:.|\n)+?)\n\n", data)

passports_parsed = []

for match in passports_raw:
    keys_values = regex.finditer(
        r"\s*(?P<key>[^:]+):(?P<value>[^\s]+)", match.group("passport")
    )
    dictionary = {}
    for key_value in keys_values:
        dictionary[key_value.group("key")] = key_value.group("value")
    passports_parsed.append(dictionary)

# Part One

valid_passports = 0

for passport in passports_parsed:
    if {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} <= passport.keys():
        valid_passports += 1

print(valid_passports)

# Part Two

valid_passports = 0

for passport in passports_parsed:
    if {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} <= passport.keys():
        if (
            (1920 <= int(passport["byr"]) <= 2002)
            and (2010 <= int(passport["iyr"]) <= 2020)
            and (2020 <= int(passport["eyr"]) <= 2030)
            and (passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
            and (len(passport["pid"]) == 9)
        ):
            height_match = regex.match(
                r"\s*(?P<height>\d+)(?P<unit>cm|in)", passport["hgt"]
            )
            if height_match and (
                (
                    height_match.group("unit") == "in"
                    and (59 <= int(height_match.group("height")) <= 76)
                )
                or (
                    height_match.group("unit") == "cm"
                    and (150 <= int(height_match.group("height")) <= 193)
                )
            ):
                hair_color_match = regex.match(
                    r"#(?P<color>(?:[0-9]|[a-f])+)", passport["hcl"]
                )
                if hair_color_match:
                    valid_passports += 1

print(valid_passports)
