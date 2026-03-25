guests = ['Urszula', 'Tadeusz', 'Paula']

print(f'Zapraszam na obiad, {guests[0]}.') # Zapraszam na obiad, Urszula.
print(f'Zapraszam na obiad, {guests[1]}.') # Zapraszam na obiad, Tadeusz.
print(f'Zapraszam na obiad, {guests[2]}.') # Zapraszam na obiad, Paula.

print(f'\nZ przykrością informuję, że {guests[1]} nie będzie mógł przyjść na obiad.\n') # Z przykrością informuję, że Tadeusz nie będzie mógł przyjść na obiad.

guests[1] = 'Krzysztof'

print(f'Zapraszam na obiad, {guests[0]}.') # Zapraszam na obiad, Urszula.
print(f'Zapraszam na obiad, {guests[1]}.') # Zapraszam na obiad, Krzysztof.
print(f'Zapraszam na obiad, {guests[2]}.') # Zapraszam na obiad, Paula.

print(f'\nZ radością informuję, że udało mi się znaleźć większy stół, więc mogę zaprosić więcej gości!\n') # Z radością informuję, że udało mi się znaleźć większy stół, więc mogę zaprosić więcej gości!   

guests.insert(0, 'Katarzyna')
guests.insert(2, 'Dawid')
guests.append('Ania')

print(f'Zapraszam na obiad, {guests[0]}.') # Zapraszam na obiad, Katarzyna.
print(f'Zapraszam na obiad, {guests[1]}.') # Zapraszam na obiad, Urszula.
print(f'Zapraszam na obiad, {guests[2]}.') # Zapraszam na obiad, Dawid.
print(f'Zapraszam na obiad, {guests[3]}.') # Zapraszam na obiad, Krzysztof.
print(f'Zapraszam na obiad, {guests[4]}.') # Zapraszam na obiad, Paula.
print(f'Zapraszam na obiad, {guests[5]}.') # Zapraszam na obiad, Ania.

print(f'Lista gości ma teraz {len(guests)} osób.') # Lista gości ma teraz 6 osób.