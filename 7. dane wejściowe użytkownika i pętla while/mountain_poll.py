responses = {}

# Ustawienie flagi wskazujacej, czy ankieta jest aktywna.
polling_active = True

while polling_active:
    # Prosba o podanie imienia uczestnika ankiety oraz odpowiedz na pytanie.
    name = input("\nJak masz na imie? ")
    response = input("Na ktory szczyt chcialbys sie wspiac pewnego dnia? ")

    # Umieszczenie odpowiedzi w slowniku:
    responses[name] = response

    # Ustalenie czy ktokolwiek jeszcze chce wziac udzial w ankiecie
    repeat = input("Czy ktokolwiek inny chce wziac udzial w ankiecie? (tak / nie) ")
    if repeat == "nie":
        polling_active = False

# Ankieta zostala zakonczona i wyswietlamy jej wyniki
print("\n--- Wyniki ankiety ---")
for name, response in responses.items():
    print(f"{name} chcialby/chcialaby sie wspiac na {response}.")
