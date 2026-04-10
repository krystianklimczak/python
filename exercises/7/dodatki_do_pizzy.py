prompt = "\nPowiedz mi, z czym chciałbyś zjeść pizzę?"
prompt += "\nJeśli nie chcesz już niczego dodawać, napisz 'koniec'. "

active = True
additions = []

while active:
    addition = input(prompt)

    if addition == "koniec":
        break
    else:
        additions.append(addition)
        print(f"Dodałeś do swojej pizzy {addition.title()}.")


if additions:
    print(f"\nNa Twojej pizzy będzie: ")
    for addition in additions:
        print(f"\t{addition.title()}")
else:
    print(f"\nTwoja pizza będzie składać się z samego ciasta!")
