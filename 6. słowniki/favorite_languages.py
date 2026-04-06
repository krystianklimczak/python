favorite_languages = {
    "janek": "python",
    "sara": "c",
    "edward": "rust",
    "paweł": "python",
}

language = favorite_languages["sara"].title()
print(f"Ulubiony język programowania Sary to {language}.")

#

for name, language in favorite_languages.items():
    print(f"\n{name.title()}, Twój ulubiony język to: {language.title()}!")

#

for name in favorite_languages.keys():  # Same as: for name in favorite_langugages:
    print(name.title())

#

friends = ["paweł", "sara"]

for name in favorite_languages.keys():
    print(f"Witaj, {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(
            f"\tWitaj, {name.title()}! Widzę, że Twoim ulubionym językiem programowania jest {language}!"
        )

#

if "elżbieta" not in favorite_languages.keys():
    print("\nElżbieta, proszę weź udział w naszej ankiecie!")

#

favorite_languages = {
    "janek": "python",
    "sara": "c",
    "edward": "rust",
    "paweł": "python",
}

for name in sorted(favorite_languages.keys()):
    print(f"\n{name.title()}, dziękujemy za udział w ankiecie.")

#

favorite_languages = {
    "janek": "python",
    "sara": "c",
    "edward": "rust",
    "paweł": "python",
}

print("\nW ankiecie zostały wymienione następujące języki programowania:")

for language in favorite_languages.values():
    print(language.title())

#

print("\nW ankiecie zostały wymienione następujące języki programowania:")
for language in set(favorite_languages.values()):
    print(language.title())

#

favorite_languages = {
    "janek": ["python", "rust"],
    "sara": ["c"],
    "edward": ["rust", "go"],
    "paweł": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\nUlubione języki programowania użytkownika {name.title()} to:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(
            f"\nUlubiony język programowania użytkownika {name.title()} to {languages[0]}"
        )

#
