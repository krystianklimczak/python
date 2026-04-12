sandwich_orders = [
    "kanapka chefa",
    "kanapka z pastrami",
    "kanapka zbója",
    "kanapka z pastrami",
    "ostra kanapka",
    "kanapka z pastrami",
]

finished_sandwiches = []

print("Uprzejmie informujemy, ze wlasnie skonczylo nam sie Pastrami.")

while "kanapka z pastrami" in sandwich_orders:
    sandwich_orders.remove("kanapka z pastrami")

while sandwich_orders:
    prepared_sandwich = sandwich_orders.pop()

    print(f"Przygotowywanie {prepared_sandwich.title()}!")

    finished_sandwiches.append(prepared_sandwich)

print("\nPrzygotowane kanapki:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
