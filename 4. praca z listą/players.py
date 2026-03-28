players = ['karol', 'martyna', 'michał', 'florian', 'ela']

print(players[0:3]) # ['karol', 'martyna', 'michał']
print(players[1:4]) # ['martyna', 'michał', 'florian']

# 

print((players[:4])) # ['karol', 'martyna', 'michał', 'florian']

# 

print(players[2:]) # ['michał', 'florian', 'ela']

# 

print(players[-3:]) # ['michał', 'florian', 'ela']

# 

print("Oto trzech pierwszych graczy naszej drużyny:")
for player in players[:3]:
    print(player.title())

# 