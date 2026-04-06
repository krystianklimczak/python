favorite_places = {
    "dawid": ["grecja", "hiszpania", "wlochy"],
    "kasia": ["francja", "szwajcaria", "dania"],
    "wiktoria": ["polska", "brazylia", "norwegia"],
}

for person, places in favorite_places.items():
    print(f"\n{person.title()} Twoje ulubione miejsca to:")
    for place in places:
        print(f"\t{place.title()}")
