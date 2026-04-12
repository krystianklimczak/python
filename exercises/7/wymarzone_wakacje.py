dreamed_holidays = {}

pooling_active = True

while pooling_active:
    user = input("Jak masz na imie? ")
    destination = input(
        "Jezeli moglbys odwiedzic jedno dowolne miejsce na swiecie, gdzie bys pojechal? "
    )

    dreamed_holidays[user] = destination

    repeat = input("Czy ktos jeszcze chce wziac udzial w ankiecie? (tak / nie) ")
    if repeat == "nie":
        pooling_active = False

print("\n--- Wyniki ankiety ---")
for user, destination in dreamed_holidays.items():
    print(f"{user.title()} chcialby odwiedzic {destination.title()}.")
