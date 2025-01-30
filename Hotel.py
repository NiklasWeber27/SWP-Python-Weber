class Room:
    def __init__(self, zimmernummer,zimmertyp, preis, verfuegbar):
        self.zimmernummer = zimmernummer
        self.zimmertyp = zimmertyp
        self.preis = preis
        self.verfuegbar = verfuegbar

    def __str__(self):
        return f'{self.zimmertyp} kostet {self.preis} Euro pro Nacht und ist verfügbar: {self.verfuegbar}'

    def book_room(self):
        self.verfuegbar = False

    def cancel_room(self):
        self.verfuegbar = True

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def anz_freerooms(self):
        anzfreerooms = len([room for room in self.rooms if room.verfuegbar])
        print(f'Anzahl freie Zimmer: {anzfreerooms}')

    def get_freerooms(self):
        anzfreerooms = [room for room in self.rooms if room.verfuegbar]
        print('Freie Zimmer:')
        for room in anzfreerooms:
            print(f"{room.zimmernummer} {room.zimmertyp}")

    def book_room(self, zimmernummer):
        for room in self.rooms:
            if room.zimmernummer == zimmernummer:
                if room.verfuegbar:
                    room.book_room()
                    print(f'{room.zimmertyp} {room.zimmernummer} wurde gebucht')
                    return
                else:
                    print(f'{room.zimmertyp} {room.zimmernummer} ist nicht verfügbar')
                    return
        print(f'Zimmer {zimmernummer} nicht gefunden')

    def cancel_room(self, zimmernummer):
        for room in self.rooms:
            if room.zimmernummer == zimmernummer:
                if room.verfuegbar:
                    print(f'{room.zimmertyp} {room.zimmernummer} ist bereits verfügbar')
                    return
                else:
                    room.cancel_room()
                    print(f'{room.zimmertyp} {room.zimmernummer} wurde storniert')
                    return
        print(f'Zimmer {zimmernummer} nicht gefunden')

def main():
    r1 = Room(1, 'Einzelzimmer', 50, True)
    r2 = Room(2, 'Doppelzimmer', 80, True)
    r3 = Room(3, 'Suite', 150, True)
    h1 = Hotel('Hilton')
    h1.add_room(r1)
    h1.add_room(r2)
    h1.add_room(r3)
    h1.anz_freerooms()
    h1.get_freerooms()
    h1.book_room(1)
    h1.anz_freerooms()
    h1.get_freerooms()
    h1.book_room(1)
    h1.book_room(4)
    h1.cancel_room(1)
    h1.anz_freerooms()
    h1.get_freerooms()


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f'Fehler: {error}')

