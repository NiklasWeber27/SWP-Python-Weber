class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age

class Player(Person):
    def __init__(self, name, age, position, club):
        super().__init__(name, age)
        self.position = position
        self.club = club

    def get_position(self):
        return self.position
    def get_club(self):
        return self.club
    def set_position(self, position):
        self.position = position
    def set_club(self, club):
        self.club = club
    def __str__(self):
        return f'{self.name} is {self.age} years old and plays as {self.position} for {self.club}'

class Trainer(Person):
    def __init__(self, name, age, club):
        super().__init__(name, age)
        self.club = club

    def get_club(self):
        return self.club
    def set_club(self, club):
        self.club = club
    def __str__(self):
        return f'{self.name} is {self.age} years old and is the trainer of {self.club}'

def main():
    p1 = Person('Jürgen', 60)
    p2 = Player('Thomas', 34, 'Midfielder', 'Fc Bayern')
    p3 = Trainer('Hansi', 60, 'Fc Barcelona')
    print(p1)
    print(p2)
    print(p3)

if __name__ == '__main__':
    main()