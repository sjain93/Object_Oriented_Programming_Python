class Cat:
    """Class about cats, enough said """

    def __init__(self, name, pref_food, meal_time):
        self.name = name
        self.preffered_food = pref_food
        self.meal_time = int(meal_time)

    def __str__(self):
        return "Cat name: {}\nMeal:{}\nMeal time:{}".format(self.name, self.preffered_food, self.meal_time)

    def eats_at(self):
        if self.meal_time > 12:
            adjusted = self.meal_time - 12
            return "{} PM".format(adjusted)
        else:
            return "{} AM".format(self.meal_time)

    def meow(self):
        return "Hi my name is {}, and I like to eat {} at {}- don't be late!".format(self.name, self.preffered_food, self.eats_at())



james = Cat("James", "Tuna", "14")
print(james)

belle = Cat("Belle", "Salmon", "18")
print(belle)



print(belle.eats_at())

statement = belle.meow()
print(statement)

statement2 = james.meow()
print(statement2)
