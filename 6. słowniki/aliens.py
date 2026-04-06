alien_0 = {"color": "zielony", "points": 5}
alien_1 = {"color": "żółty", "points": 10}
alien_2 = {"color": "czerwony", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#

# Utworzenie pustej listy przeznaczonej do przechowywania obcych.
aliens = []

# Utworzenie 30 zielonych obcych.
for alien_number in range(30):
    new_alien = {"color": "zielony", "points": 5, "speed": "wolno"}
    aliens.append(new_alien)

# Wyświetlanie pierszych pięciu obcych.
for alien in aliens[:5]:
    print(alien)
print("...")

# Wyświetlanie całkowitej liczby utworzonych obcych.
print(f"Całkowita liczba obcych: {len(aliens)}\n")

#

for alien in aliens[0:3]:
    if alien["color"] == "zielony":
        alien["color"] = "żółty"
        alien["speed"] = "średnio"
        alien["points"] = 10

# Wyświetlenie pierwszych pięciu obcych:
for alien in aliens[:5]:
    print(alien)
print("...")

#

for alien in aliens[0:3]:
    if alien["color"] == "zielony":
        alien["color"] = "żółty"
        alien["speed"] = "średnio"
        alien["points"] = 10
    elif alien["color"] == "żółty":
        alien["color"] = "czerwony"
        alien["speed"] = "szybko"
        alien["points"] = 15

# Wyświetlenie pierwszych pięciu obcych:
for alien in aliens[:5]:
    print(alien)
print("...")
