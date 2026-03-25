cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort() # metoda sort() sortuje trwale listę alfabetycznie 
print(cars)

# 

cars.sort(reverse=True) # metoda sort() z argumentem reverse=True sortuje trwale listę w odwrotnej kolejności alfabetycznej
print(cars)

# 

cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Oto lista początkowa:')
print(cars)

print("\nOto lista posortowana")
print(sorted(cars)) # funkcja sorted() sortuje tymczasowo listę alfabetycznie. Funkcja sorted() również przyjmuje argument reverse=True.

print("\nOto ponownie lista początkowa:")
print(cars)

# 

print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse() # metoda reverse() odwraca trwale kolejność elementów na liście.
print(cars)

# 

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) # funkcja len() zwraca długość listy, czyli liczbę elementów na liście.