current_users = ['Eryk', 'Ala', 'Kasia', 'Dawid', 'Robert']

new_users = ['Eryk', 'Magda', 'Krystian', 'kasia']

for new_user in new_users:
    if new_user in current_users:
        print(f"Nazwa użytkownika {new_user} jest już zajęta. Wybierz inną nazwę użytkownika.")
    else:
        print(f"Nazwa użytkownika {new_user} jest dostępna.")

current_users_lower = []

for current_user in current_users:
    current_users_lower.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Nazwa użytkownika {new_user} jest już zajęta. Wybierz inną nazwę użytkownika.")
    else:
        print(f"Nazwa użytkownika {new_user} jest dostępna.")

