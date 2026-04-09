number = input("Proszę podać dowolną liczbę: ")

number = int(number)

if number % 10 == 0:
    print(f"Podana liczba {number} jest wielokrotnością liczby 10.")
else:
    print(f"Podana liczba {number} nie jest wielokrotnością liczby 10.")
