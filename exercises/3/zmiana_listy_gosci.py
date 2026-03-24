guests = ['Urszula', 'Tadeusz', 'Paula']

print(f'Zapraszam na obiad, {guests[0]}.') # Zapraszam na obiad, Urszula.
print(f'Zapraszam na obiad, {guests[1]}.') # Zapraszam na obiad, Tadeusz.
print(f'Zapraszam na obiad, {guests[2]}.') # Zapraszam na obiad, Paula.

print(f'\nZ przykrością informuję, że {guests[1]} nie będzie mógł przyjść na obiad.\n') # Z przykrością informuję, że Tadeusz nie będzie mógł przyjść na obiad.

guests[1] = 'Krzysztof'

print(f'Zapraszam na obiad, {guests[0]}.') # Zapraszam na obiad, Urszula.
print(f'Zapraszam na obiad, {guests[1]}.') # Zapraszam na obiad, Krzysztof.
print(f'Zapraszam na obiad, {guests[2]}.') # Zapraszam na obiad, Paula.
