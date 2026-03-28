dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])

# 

# dimensions[0] = 250 # TypeError: 'tuple' object does not support item assignment

# 

my_t = (3,)

# 

for dimension in dimensions:
    print(dimension)

# 

print("Wymiary początkowe:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)

print("\nWymiary po modyfikacji:")
for dimension in dimensions:
    print(dimension)

# 