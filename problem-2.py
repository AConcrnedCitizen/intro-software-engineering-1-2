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

vegetarian = input("Is anyone in your party a vegetarian? ")
vegetarian = True if vegetarian.lower().startswith('y') else False

vegan = input("Is anyone in your party a vegan? ")
vegan = True if vegan.lower().startswith('y') else False

gluten_free = input("Is anyone in your party gluten-free? ")
gluten_free = True if gluten_free.lower().startswith('y') else False

print("Here are your restaurant choices:\n\n")
for resturaunt in resturaunts:
    if (vegetarian and resturaunts[resturaunt]["vegetarian"]) or (vegan and resturaunts[resturaunt]["vegan"]) or (gluten_free and resturaunts[resturaunt]["gluten-free"]):
        print(resturaunt)
          