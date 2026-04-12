sandwich_orders = ["kanapka chefa", "kanapka zbója", "ostra kanapka"]

finished_sandwiches = []

while sandwich_orders:
    prepared_sandwich = sandwich_orders.pop()
    print(f"Przygotowywanie {prepared_sandwich.title()}!")

    finished_sandwiches.append(prepared_sandwich)

print("\nPrzygotowane kanapki:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
