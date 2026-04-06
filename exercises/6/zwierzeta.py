pet_0 = {
    "name": "azor",
    "species": "pies",
    "owner": "bob",
    "age": 2,
}

pet_1 = {
    "name": "mruczek",
    "species": "kot",
    "owner": "nami",
    "age": 7,
}

pet_2 = {
    "name": "grzywacz",
    "species": "koń",
    "owner": "garcia",
    "age": "4",
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    pet_name = pet["name"]
    pet_owner = pet["owner"]
    pet_species = pet["species"]
    pet_age = pet["age"]

    print(f"Zwierzę o imieniu {pet_name.title()} to {pet_species}.")
    print(f"Aktualnie jest w wieku {pet_age} lat.")
    print(f"Jego właścicielem jest {pet_owner.title()}.\n")
