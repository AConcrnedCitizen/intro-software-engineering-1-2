# Dict of resturaunts with their dietary options
resturaunts = {
    "Joe's Gourmet Burgers": {
        "vegetarian": False,
        "vegan": False,
        "gluten-free": False
    },
    "Main Street Pizza Company": {
        "vegetarian": True,
        "vegan": False,
        "gluten-free": True
    },
    "Corner Cafe": {
        "vegetarian": True,
        "vegan": True,
        "gluten-free": True
    },
    "Mama's Fine Italian": {
        "vegetarian": True,
        "vegan": False,
        "gluten-free": False
    },
    "The Chef's Kitchen": {
        "vegetarian": True,
        "vegan": True,
        "gluten-free": True
    }
}

print("ANSWER THE FOLLOWING QUESTIONS WITH 'yes' OR 'no'")

# Function that takes the answer and interprets it as a boolean
def parse_answer(answer):
    return True if answer.startswith("y") else False

# Asks the user if they are vegetarian, vegan, or gluten-free
vegetarian = parse_answer(input("Are you vegetarian? "))
vegan = parse_answer(input("Are you vegan? "))
gluten_free = parse_answer(input("Are you gluten-free? "))

for resturaunt in resturaunts:
    if not vegetarian and resturaunts[resturaunt]["vegetarian"]:
        continue
    if not vegan and resturaunts[resturaunt]["vegan"]:
        continue
    if not gluten_free and resturaunts[resturaunt]["gluten-free"]:
        continue
    print(resturaunt)
