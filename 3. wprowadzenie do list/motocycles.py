motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles) # ['honda', 'yamaha', 'suzuki']

# 

motorcycles[0] = 'ducati'

print(motorcycles) # ['ducati', 'yamaha', 'suzuki']

# 

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')

print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'ducati']
# Metoda append() sprawia, że element 'ducati' zostaje umieszczony na końcu listy, a pozostałe elementy nie zostają w żaden sposób zmodyfikowane.

#
#  
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles) # ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')

print(motorcycles) # ['ducati', 'honda', 'yamaha', 'suzuki']
# Nowy element można wstawić w dowolnie wybranym miejscu listy, używając do tego metody insert(). Argumentami tej metody są indeks dla nowego elemntu oraz jego wartość.


motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles) # ['yamaha', 'suzuki']
# Za pomocą polecenia del możesz usunąć dowolny element z listy, o ile znasz jego indeks.


motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles) # ['honda', 'yamaha']
print(popped_motorcycle) # suzuki
# Metoda pop() powoduje usunięcie ostatniego elementu z listy, ale pozwala na pracę z nim jeszcze po jego usunięciu.

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"Mój pierwszy motocykl to {first_owned.title()}.") # Mój pierwszy motocykl to Honda.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.remove('ducati')
print(motorcycles) # ['honda', 'yamaha', 'suzuki']
# Metoda remove() pozwala usunąć element z listy, ale musisz znać jego wartość, a nie indeks. Jeśli w liście znajduje się więcej niż jeden taki element, metoda remove() usunie tylko pierwszy z nich. Jeśli element, który chcesz usunąć, nie znajduje się w liście, Python zwróci błąd.

motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles[3]) # IndexError: list index out of range
# Jeśli próbujesz uzyskać dostęp do elementu, którego indeks jest poza zakresem, Python zwróci błąd IndexError. W powyższym przykładzie lista motorcycles zawiera tylko trzy elementy, więc indeks 3 jest poza zakresem.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1]) # suzuki
#  Indeks -1 zawsze zwraca ostatni element listy, którym w omawianym przykładzie jest 'suzuki'.

