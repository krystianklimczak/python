favourite_numbers = {
    "krystian": 15,
    "ania": 8,
    "arina": 11,
    "paula": 29,
    "kazimierz": 13,
}

print(f"Ulubiona liczba Krystiana to: {favourite_numbers['krystian']}.")
print(f"Ulubiona liczba Ani to: {favourite_numbers['ania']}.")
print(f"Ulubiona liczba Ariny to: {favourite_numbers['arina']}.")
print(f"Ulubiona liczba Pauli to: {favourite_numbers['paula']}.")
print(f"Ulubiona liczba Kazimierza to: {favourite_numbers['kazimierz']}.")

#

favorite_numbers = {
    "krystian": [15, 96],
    "ania": [12, 25],
    "arina": [7, 5],
    "paula": [29, 13],
}

for person, fav_nums in favorite_numbers.items():
    print(f"\nUlubione liczby użytkownika {person.title()} to:")
    for num in fav_nums:
        print(f"\t{num}")
