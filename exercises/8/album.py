def make_album(band_name, album_title):
    album = {"band": band_name, "title": album_title}
    return album


first_album = make_album("tokyo rangers", "into cosmo")
print(first_album)

second_album = make_album("nusty cats", "miau")
print(second_album)


def make_album(band_name, album_title, songs=None):
    album = {"band": band_name, "title": album_title}
    if songs:
        album["songs"] = songs
    return album


third_album = make_album("crazy bananas", "monkeys on tree", 18)
print(third_album)
