class Vampire:
    coven = []

    @classmethod
    def create(cls, name, age):
        new_vampire = Vampire(name, age)
        cls.coven.append(new_vampire)
        return new_vampire

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.in_coffin = False
        self.drank_blood_today = False

    def drink_blood(self):
        self.drank_blood_today = True

    def go_home(self):
        self.in_coffin = True

    @classmethod
    def sunrise(cls):
        for vampire in Vampire.coven:
            if vampire.in_coffin == False or vampire.drank_blood_today == False:
                Vampire.coven.remove(vampire)

    @classmethod
    def sunset(cls):
        for vampire in cls.coven:
            vampire.in_coffin = False
            vampire.drank_blood_today = False

vampire1 = Vampire.create("Edward", 150)
vampire2 = Vampire.create("Dracula", 500)
vampire3 = Vampire.create("Bob", 400)

print(Vampire.coven)
vampire1.go_home()
print(vampire1.in_coffin)

vampire1.drink_blood()
print(Vampire.coven)

Vampire.sunrise()
print(Vampire.coven[0].in_coffin)
