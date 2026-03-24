motorcycles = ['honda', 'yamaha', 'suzuki']

# print(motorcycles) # ['honda', 'yamaha', 'suzuki']

# motorcycles[0] = 'ducati'

# print(motorcycles) # ['ducati', 'yamaha', 'suzuki']

# motorcycles.append('ducati')

# print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'ducati']
# Metoda append() sprawia, że element 'ducati' zostaje umieszczony na końcu listy, a pozostałe elementy nie zostają w żaden sposób zmodyfikowane.

# motorcycles = []

# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')

# print(motorcycles) # ['honda', 'yamaha', 'suzuki']

# motorcycles.insert(0, 'ducati')

# print(motorcycles) # ['ducati', 'honda', 'yamaha', 'suzuki']
# Nowy element można wstawić w dowolnie wybranym miejscu listy, używając do tego metody insert(). Argumentami tej metody są indeks dla nowego elemntu oraz jego wartość.

# del motorcycles[0]
# print(motorcycles) # ['yamaha', 'suzuki']
# Za pomocą polecenia del możesz usunąć dowolny element z listy, o ile znasz jego indeks.

# popped_motorcycle = motorcycles.pop()
# print(motorcycles) # ['honda', 'yamaha']
# print(popped_motorcycle) # suzuki
# Metoda pop() powoduje usunięcie ostatniego elementu z listy, ale pozwala na pracę z nim jeszcze po jego usunięciu.

# first_owned = motorcycles.pop(0)
# print(f"Mój pierwszy motocykl to {first_owned.title()}.") # Mój pierwszy motocykl to Honda.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.remove('ducati')
print(motorcycles) # ['honda', 'yamaha', 'suzuki']
# Metoda remove() pozwala usunąć element z listy, ale musisz znać jego wartość, a nie indeks. Jeśli w liście znajduje się więcej niż jeden taki element, metoda remove() usunie tylko pierwszy z nich. Jeśli element, który chcesz usunąć, nie znajduje się w liście, Python zwróci błąd.