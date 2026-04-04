alien_0 = {"color": "zielony", "speed": "wolno"}

# KeyError: 'points'

# print(alien_0["points"])

# KeyError: 'points'

#

alien_0 = {"color": "zielony", "speed": "wolno"}

point_value = alien_0.get("points", "Brak przypisanych punktów.")

print(point_value)

#
