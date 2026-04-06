person_0 = {
    "first_name": "krystian",
    "last_name": "klimczak",
    "age": 29,
    "city": "glogau",
}

person_1 = {
    "first_name": "ania",
    "last_name": "istochnikova",
    "age": 29,
    "city": "ascheberg",
}

person_2 = {
    "first_name": "arina",
    "last_name": "istochnikova",
    "age": 17,
    "city": "warsaw",
}

people = [person_0, person_1, person_2]

for person in people:
    user = f"{person['first_name']} {person['last_name']}"
    age = person["age"]
    location = person["city"]

    print(
        f"Uzytkownik {user.title()}, ma {age} lat i zamieszkuje w {location.title()}."
    )
