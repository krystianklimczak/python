def make_album(band_name, album_title, songs=None):
    album = {"band": band_name, "title": album_title}
    if songs:
        album["songs"] = songs
    return album


while True:
    print(f"\nProszę podać nazwę zespołu oraz nazwę albumu: ")
    print("(aby wyjść z programu, wpisz 'q' i zatwierdź enterem)")

    b_name = input("Nazwa zespołu: ")
    if b_name == "q":
        break

    a_title = input("Nazwa albumu: ")
    if a_title == "q":
        break

    album = make_album(b_name, a_title)
    print(f"\n{album}")
