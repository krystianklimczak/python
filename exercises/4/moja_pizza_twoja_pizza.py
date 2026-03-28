pizzas = ['margarita', 'pepperoni', 'hawaiian', 'calzone', 'veggie']

friend_pizzas = pizzas[:]

# 

pizzas.append('meat lovers')
friend_pizzas.append('vegan')

# 

print("Moje ulubione rodzaje pizzy to:")
for pizza in pizzas:
    print(pizza)


print("\nUlubione rodzaje pizzy mojego przyjaciela to:")
for pizza in friend_pizzas:
    print(pizza)