# users = ['admin', 'Eryk', 'Ala', 'Kasia', 'Dawid']
users = []

if users:
    for user in users:
        if user == 'admin':
            print(f"Witaj, {user}! Czy chcesz przejrzeć dzisiejszy raport?")
        else:
            print(f"Witaj, {user}! Dziękujemy, że ponownie się zalogowałeś.")
else:
    print("Musimy znaleźć jakichś użytkowników!")