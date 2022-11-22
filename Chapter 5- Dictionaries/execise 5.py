pets = []


pet = {
    ("animal type"): ("python"),
    ("name"): ("john"),
    ("owner"): ("guido"),
    ("weight"): 44,
    ("eats"): ("bugs"),
}
pets.append(pet)

pet = {
    ("animal type"): ("chicken"),
    ("name"): ("bekoo"),
    ("owner"): ("lost of hen"),
    ("weight"): 4,
    ("eats"): ("seeds"),
}
pets.append(pets)

pet = {
    ("animal type"): ("dog"),
    ("name"): ("Max"),
    ("owner"): ("scott"),
    ("weight"): 36,
    ("eats"): ("shoes"),
}
pets.append(pet)


for pet in pets:
    print("\nHere's what I know about " + pet ["name"].title()
    for key, value in pet.items()
       print("\t" + key + ": " + str(value))