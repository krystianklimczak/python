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

print(f'\nNiestety, stół będzie dostarczony dopiero jutro, więc mogę zaprosić tylko dwóch gości.\n') # Niestety, stół będzie dostarczony dopiero jutro, więc mogę zaprosić tylko dwóch gości.

print(f'Przepraszam, {guests.pop(0)}, ale nie będziesz mógł przyjść na obiad.') # Przepraszam, Katarzyna, ale nie będziesz mógł przyjść na obiad.
print(f'Przepraszam, {guests.pop(1)}, ale nie będziesz mógł przyjść na obiad.') # Przepraszam, Dawid, ale nie będziesz mógł przyjść na obiad.
print(f'Przepraszam, {guests.pop(1)}, ale nie będziesz mógł przyjść na obiad.') # Przepraszam, Krzysztof, ale nie będziesz mógł przyjść na obiad.
print(f'Przepraszam, {guests.pop(2)}, ale nie będziesz mógł przyjść na obiad.') # Przepraszam, Ania, ale nie będziesz mógł przyjść na obiad.

print('')
print(f'Zapraszam na obiad, {guests[0]}.') # Zapraszam na obiad, Urszula.
print(f'Zapraszam na obiad, {guests[1]}.') # Zapraszam na obiad, Paula.

del guests[0]
del guests[0]

print('')
print(guests) # []