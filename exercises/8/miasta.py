def describe_city(city, country="polsce"):
    """Wyświetla informacje o mieście."""
    print(f"\nMiasto {city.title()} leży w {country.title()}.")


describe_city("warszawa")
describe_city("głogów")
describe_city("berlin", "niemczech")
