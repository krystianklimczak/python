numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f"{number}st,")
    elif number == 2:
        print(f"{number}nd,")
    elif number == 3:
        print(f"{number}rd,")
    else:
        print(f"{number}th,")

# 

text = ''

for number in numbers:
    if number == 1:
        text += ("1st,")
    elif number == 2:
        text += (" 2nd,")
    elif number == 3:
        text += (" 3rd,")
    else:
        text += (f" {number}th,")

print(f"\n{text}")