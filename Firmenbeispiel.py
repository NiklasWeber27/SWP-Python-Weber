class Person:
    def __init__(self, name, is_male):
        self.name = name
        self.is_male = is_male

    def __str__(self):
        return f'{self.name} is a male? {self.is_male}'

    def __repr__(self):
        return f'Person(\'{self.name}\', {self.is_male})'

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_is_male(self):
        return self.is_male

    def set_is_male(self, is_male):
        self.is_male = is_male

class Mitarbeiter(Person):
    def __init__(self, name, is_male, abteilung):
        super().__init__(name, is_male)
        self.abteilung = abteilung

    def __str__(self):
        return f'{self.name} works in {self.abteilung}, is a male? {self.is_male}'

    def __repr__(self):
        return f'Mitarbeiter(\'{self.name}\' , {self.is_male}, \'{self.abteilung}\')'

    def get_abteilung(self):
        return self.abteilung

    def set_abteilung(self, abteilung):
        self.abteilung = abteilung

class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name: str, is_male: bool, abteilung):
        super().__init__(name, is_male, abteilung)

    def __str__(self):
        return f'{self.name} is the head of {self.abteilung}, is a male? {self.is_male}'

class Abteilung:
    def __init__(self, name, abteilungsleiter):
        self.name = name
        self.abteilungsleiter = abteilungsleiter
        self.mitarbeiter = []

    def __str__(self):
        return f'{self.name} is led by {self.abteilungsleiter.get_name()}'

    def __repr__(self):
        return f'Abteilung(\'{self.name}\', \'{self.abteilungsleiter.get_name()}\')'

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_abteilungsleiter(self):
        return self.abteilungsleiter

    def set_abteilungsleiter(self, abteilungsleiter):
        self.abteilungsleiter = abteilungsleiter

    def get_mitarbeiter(self):
        return self.mitarbeiter

    def set_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter = mitarbeiter

    def add_mitarbeiter(self, mitarbeiter: Mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def __str__(self):
        return f'{self.name} has {len(self.abteilungen)} departments'

    def __repr__(self):
        return f'Firma(\'{self.name}\')'

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_abteilungen(self):
        return self.abteilungen

    def set_abteilungen(self, abteilungen):
        self.abteilungen = abteilungen

    def add_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def anz_mitarbeiter(self):
        return sum(len(abteilung.mitarbeiter) for abteilung in self.abteilungen)

    def anz_abteilungsleiter(self):
        return len(self.abteilungen)

    def anz_abteilungen(self):
        return len(self.abteilungen)

    def abt_most_mitarbeiter(self):
        maxWorkerAbt = 0
        abtName = ""
        for abteilung in self.abteilungen:
            if len(abteilung.mitarbeiter) > maxWorkerAbt:
                maxWorkerAbt = len(abteilung.mitarbeiter)
                abtName = abteilung.name
        print(abtName, maxWorkerAbt)

    def prozent_frauen_maenner(self):
        gesamt = [mitarbeiter for abteilung in self.abteilungen for mitarbeiter in abteilung.mitarbeiter]
        gesamtanzahl = self.anz_mitarbeiter()

        if gesamtanzahl == 0:
            return {"frauen": 0, "maenner": 0}

        frauen_prozent = sum(1 for mitarbeiter in gesamt if not mitarbeiter.is_male) / gesamtanzahl * 100
        maenner_prozent = 100 - frauen_prozent

        return {"frauen": frauen_prozent, "maenner": maenner_prozent}


def main():
    p1 = Person('Herbert', True)
    print(p1)
    m1 = Mitarbeiter('Hans', True, 'IT')
    m2 = Mitarbeiter('Gabi', False, 'HR')
    print(m1)
    a1 = Abteilungsleiter('Klaus', True, 'IT')
    print(a1)
    abt1 = Abteilung('IT', a1)
    abt1.add_mitarbeiter(m1)
    abt1.add_mitarbeiter(m2)
    print(abt1)
    f1 = Firma('Firma1')
    f1.add_abteilung(abt1)
    print(f1)
    print(f1.anz_mitarbeiter())
    print(f1.anz_abteilungsleiter())
    print(f1.anz_abteilungen())
    f1.abt_most_mitarbeiter()
    print(f1.prozent_frauen_maenner())



if __name__ == '__main__':
    main()