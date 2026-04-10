# message = input("Powiedz mi coś o sobie, a wyświetlę to na ekranie: ")
# print(message)

prompt = "\nPowiedz mi coś o sobie, a wyświetlę to na ekranie:"
prompt += "\nNapisz 'koniec', aby zakończyć działanie programu. "

# message = ""

# while message != "koniec":
#     message = input(prompt)

#     if message != "koniec":
#         print(f"\n\t{message}")

active = True

while active:
    message = input(prompt)

    if message == "koniec":
        active = False
    else:
        print(message)
