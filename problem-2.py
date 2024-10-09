'''
*******************************
Author:
u3275885
Assignment:
Assessment 2 - Problem 2
4/10/2024
*******************************
'''
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
    if answer.startswith("y") or answer.startswith("n"):
        return True if answer.startswith("y") else False
    
    raise ValueError("Invalid answer")

# Asks the user if they are vegetarian, vegan, or gluten-free
vegetarian = parse_answer(input("Are you vegetarian? "))
vegan = parse_answer(input("Are you vegan? "))
gluten_free = parse_answer(input("Are you gluten-free? "))

# For each one
for resturaunt in resturaunts:
    # If the user is not vegetarian and the resturaunt is vegetarian, skip
    if vegetarian and not resturaunts[resturaunt]["vegetarian"]:
        continue
    if vegan and not resturaunts[resturaunt]["vegan"]:
        continue
    if gluten_free and not resturaunts[resturaunt]["gluten-free"]:
        continue
    # Print the resturaunt because it meets the dietary requirements
    print(resturaunt)
