favorite_languages = {
    "janek": "python",
    "sara": "c",
    "edward": "rust",
    "paweł": "python",
}

people = ["janek", "katarzyna", "edward", "sylwia"]

for person in people:
    if person in favorite_languages.keys():
        print(f"Dzięki {person.title()}, za wzięcie udziału w ankiecie!")
    else:
        print(f"{person.title()}, zapraszamy do wzięcia udziału w ankiecie!")
