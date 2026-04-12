prompt = "Aby kupić bilet do kina, powiedz ile masz lat? "

while True:
    message = input(prompt)

    user_age = int(message)

    if user_age < 3:
        print(f"Bilet dla osób w Twoim wieku jest bezpłatny!")
        break
    elif user_age <= 12:
        print(f"Bilet dla osób w Twoim wieku kosztuje 10zł.")
        break
    else:
        print(f"Bilet dla osób w Twoim wieku kosztuje 15 zł.")
        break
