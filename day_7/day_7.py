import regex

with open("day_7/input.txt", "r") as myfile:
    rows = myfile.readlines()

rules = {}
for row in rows:
    match = regex.match(r"(?P<bag>.*?)\s+bags?\s+contain\s+(?P<children>.*)", row)
    rule = {}
    rule_matches = list(
        regex.finditer(
            r"(?P<number>\d+)\s+(?P<bag>.*?)\s+bags?[,.]", match.group("children")
        )
    )
    for rule_match in rule_matches:
        rule[rule_match.group("bag")] = int(rule_match.group("number"))
    rules[match.group("bag")] = {"child_rules": rule, "contains": -1}


# Part One


def check_possibilities(rule: str, look_for: str) -> bool:
    if len(rules[rule]["child_rules"]) == 0:
        return 0
    if look_for in rules[rule]["child_rules"]:
        return 1
    filtered_rules = [
        x for x in rules[rule]["child_rules"] if rules[x]["contains"] != 0
    ]
    for rule_test in filtered_rules:
        rules[rule_test]["contains"] = check_possibilities(rule_test, look_for)
    return 0 if not any(rules[rule]["contains"] == 1 for rule in filtered_rules) else 1


occurences = 0

for rule in rules:
    if rules[rule]["contains"] == -1:
        rules[rule]["contains"] = check_possibilities(rule, "shiny gold")
    if rules[rule]["contains"] == 1:
        occurences += 1

print(occurences)


# Part Two


def count_children(rule: str) -> int:
    counter = 1
    for children in rules[rule]["child_rules"]:
        counter += rules[rule]["child_rules"][children] * count_children(children)
    return counter


print(count_children("shiny gold") - 1)
