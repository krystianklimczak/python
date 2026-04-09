reservation = input("Na ile osób chciałbyś zarezerwować stolik? ")

reservation = int(reservation)

if reservation <= 8:
    print(f"\nStolik jest gotowy, zapraszam za mną.")
else:
    print(
        f"\nProszę zaczekać, sprawdzimy czy mamy gotowy stolik na {reservation} osób."
    )
