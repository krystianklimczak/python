age = 12

if age < 4:
    print("Cena biletu wstępu wynosi 0 zł.")
elif age < 18:
    print("Cena biletu wstępu wynosi 25 zł.")
else:
    print("Cena biletu wstępu wynosi 40 zł.")

# 

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"\nCena biletu wstępu wynosi {price} zł.")

# 

age = 67

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"\nCena biletu wstępu wynosi {price} zł.")

# 

age = 67

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"\nCena biletu wstępu wynosi {price} zł.")