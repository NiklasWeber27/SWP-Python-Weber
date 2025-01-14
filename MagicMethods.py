class Auto:
    def __init__(self, ps):
        if not isinstance(ps, int) or ps <= 0:
            raise ValueError("PS muss positiv sein und eine Ganzzahl")
        self.ps = ps

    def __add__(self, other):
        if not isinstance(other, Auto):
            raise ValueError('Nur Autos können miteinander addiert werden')
        return self.ps + other.ps

    def __sub__(self, other):
        if not isinstance(other, Auto):
            raise ValueError('Nur Autos können miteinander subtrahiert werden')
        return self.ps - other.ps

    def __mul__(self, other):
        if not isinstance(other, Auto):
            raise ValueError('Nur Autos können miteinander multipliziert werden')
        return self.ps * other.ps

    def __truediv__(self, other):
        if not isinstance(other, Auto):
            raise ValueError('Nur Autos können miteinander dividiert werden')
        return self.ps / other.ps

    def __eq__(self, other):
        if not isinstance(other, Auto):
            raise ValueError('Nur Autos können miteinander verglichen werden')
        return self.ps == other.ps

    def __lt__(self, other):
        if not isinstance(other, Auto):
            raise ValueError('Nur Autos können miteinander verglichen werden')
        return self.ps < other.ps

    def __gt__(self, other):
        if not isinstance(other, Auto):
            raise ValueError('Nur Autos können miteinander verglichen werden')
        return self.ps > other.ps

def main():
    a1 = Auto(100)
    a2 = Auto(50)
    print(a1 +a2)
    print(a1 - a2)
    print(a1 * a2)
    print(a1 / a2)
    print(a1 == a2)
    print(a1 < a2)
    print(a1 > a2)


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f'Fehler: {error}')

