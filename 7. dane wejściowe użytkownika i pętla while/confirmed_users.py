# Rozpoczynamy od użytkowników, ktorzy maja byc zweryfikowani.
# Tworzymy tez pusta liste przeznaczona do przechowywania zweryfikowanych uzytkownikow.
unconfirmed_users = ["alicja", "bartek", "katarzyna"]
confirmed_users = []

# Weryfikujemy poszczegolnych uzytkownikow, dopoki lista nie bedzie pusta.
# Kazdego zweryfikowanego uzytkownika przenosimy na oddzielna liste.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Weryfikacja uzytkownika: {current_user.title()}")
    confirmed_users.append(current_user)

# Wyswietlenie wszystkich zweryfikowanych uzytkownikow.
print("\nZweryfikowano wymienionych ponizej uzytkownikow:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
