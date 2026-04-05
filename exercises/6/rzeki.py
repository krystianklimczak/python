rivers = {
    "nil": "egipt",
    "dunaj": "niemcy",
    "ren": "szwajcaria",
    "wolga": "rosja",
    "wisła": "polska",
}

for key, value in rivers.items():
    print(f"\n{key.title()} przepływa przez {value.title()}.")

#
print("\nRzeki:")
for key in rivers.keys():
    print(f"{key.title()}")

#

print("\nPaństwa:")
for value in rivers.values():
    print(f"{value.title()}")
