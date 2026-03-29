new_car = 'audi'
old_car = 'toyota'

print(f"Czy nowy samochód jest równy staremu? new_car == old_car")
print(new_car == old_car)

# 

current_user = 'Krystian'
new_user = 'krystian'

print(f"Czy nowy użytkownik znajduje się wśród obecnych użytkowników? new_user == current_user")
print(new_user.lower() == current_user.lower())

# 

age = 17
neccessary_age = 18

print(f"Czy wiek jest większy lub równy wymaganemu? age >= neccessary_age")
print(age >= neccessary_age)

print(f"Czy wiek jest mniejszy lub równy wymaganemu? age <= neccessary_age")
print(age <= neccessary_age)

# 

number = 13

quess_number_1 = 7
quess_number_2 = 13

print(f"Czy quess number 1 oraz 2 są poprawne? quess_number_1 == number and quess_number_2 == number")
print(quess_number_1 == number and quess_number_2 == number)

print(f"Czy quess number 1 lub 2 jest poprawne? quess_number_1 == number or quess_number_2 == number")
print(quess_number_1 == number or quess_number_2 == number)

# 

dogs = ['buldog', 'labrador', 'pudel']
my_dog = 'buldog'

print(f"Czy mój pies znajduje się wśród psów na liście? my_dog in dogs")
print(my_dog in dogs)

print(f"Czy mój pies nie znajduje się wśród psów na liście? my_dog not in dogs")
print(my_dog not in dogs)