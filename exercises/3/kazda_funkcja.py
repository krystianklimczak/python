languages = ['english', 'polish', 'german', 'french', 'italian', 'spanish', 'portuguese', 'russian', 'japanese', 'chinese']

print('Lista języków:')
print(languages)

languages.reverse()
print('\nLista języków w odwrotnej kolejności:')
print(languages)

languages.sort()
print('\nLista języków posortowana alfabetycznie:')
print(languages)

languages.sort(reverse=True)
print('\nLista języków posortowana w odwrotnej kolejności alfabetycznej:')
print(languages)

print(f'\nIlość języków: {len(languages)}.')

