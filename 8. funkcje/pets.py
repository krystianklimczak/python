def describe_pet(animal_type, pet_name):
    """Wyświetla informacje o zwierzęciu."""
    print(f"\nMoje zwierzę to {animal_type}.")
    print(f"Mój {animal_type} ma na imię {pet_name.title()}.")


describe_pet("chomik", "harry")
describe_pet("pies", "willie")


def describe_pet(animal_type, pet_name):
    """Wyświetla informacje o zwierzęciu."""
    print(f"\nMoje zwierzę to {animal_type}.")
    print(f"Mój {animal_type} ma na imię {pet_name.title()}.")


describe_pet(animal_type="chomik", pet_name="harry")


def describe_pet(pet_name, animal_type="pies"):
    """Wyświetla informacje o zwierzęciu."""
    print(f"\nMoje zwierzę to {animal_type}.")
    print(f"Mój {animal_type} ma na imię {pet_name.title()}.")


describe_pet(pet_name="willie")
