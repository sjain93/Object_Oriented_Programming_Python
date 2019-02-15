class Cat:
    """Class about cats, enough said """

    def __init__(self, name, pref_food, meal_time):
        self.name = name
        self.preffered_food = pref_food
        self.meal_time = meal_time

    def __str__(self):
        return "Hi my name is {}, and I like to eat {} at {}- don't be late!".format(self.name, self.preffered_food, self.meal_time)


james = Cat("James", "Tuna", "14")
print(james)

belle = Cat("Belle", "Salmon", "18")
print(james)
