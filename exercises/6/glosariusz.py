glosariusz = {
    "variable": "Zmienna to miejsce w pamięci komputera, gdzie przechowujemy dane, które mogą się zmieniać podczas wykonywania programu.",
    "string": "Ciąg znaków (string) to typ danych reprezentujący tekst, składający się z sekwencji znaków.",
    "number": "Liczba to typ danych reprezentujący wartości numeryczne, takie jak całkowite (int) lub zmiennoprzecinkowe (float).",
    "comment": "Komentarz to tekst w kodzie źródłowym, który jest ignorowany przez interpreter Pythona i służy do wyjaśnień dla programistów.",
    "list": "Lista to struktura danych przechowująca uporządkowaną kolekcję elementów, które mogą być modyfikowane.",
    "for_loop": "Pętla for to konstrukcja programistyczna pozwalająca na wielokrotne wykonanie bloku kodu dla każdego elementu w sekwencji.",
    "tuple": "Krotka to niemutowalna struktura danych przechowująca uporządkowaną kolekcję elementów, podobna do listy, ale niezmienna.",
    "dictionary": "Słownik to struktura danych przechowująca pary klucz-wartość, umożliwiająca szybki dostęp do wartości poprzez unikalne klucze.",
}

print("Veriable:")
print(f'\t{glosariusz["variable"]}')

print("\nString:")
print(f'\t{glosariusz["string"]}')

print("\nNumber:")
print(f"\t{glosariusz['number']}")

print("\nComment:")
print(f"\t{glosariusz['comment']}")

print("\nList:")
print(f"\t{glosariusz['list']}")

print("\nFor loop:")
print(f"\t{glosariusz['for_loop']}")

print("\nTuple:")
print(f"\t{glosariusz['tuple']}")

print("\nDictionary:")
print(f"\t{glosariusz['dictionary']}")

#

for key, value in glosariusz.items():
    print(f"\n{key.title()}:")
    print(f"\t{value}")
