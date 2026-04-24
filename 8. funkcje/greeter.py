def greet_user():
    """Wyświetla proste powitanie."""
    print("Witaj!")


greet_user()

#


def greet_user(username):
    """Wyświetla proste powitanie."""
    print(f"Witaj, {username.title()}!")


greet_user("janek")
greet_user("sara")
