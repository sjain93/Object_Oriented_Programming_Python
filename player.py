class player:
    """ A class representing a player"""

    def __init__(self, gold_coins = 0, health_points = 10, lives = 5):
        self.gold_coins = int(gold_coins)
        self.health_points = int(health_points)
        self.lives= int(lives)

    def __str__(self):
        return "Player Gold coins:{}\nPlayer HP:{}\nPlayer lives:{}".format(self.gold_coins, self.health_points, self.lives)

    def level_up(self):
        self.lives = self.lives + 1

    def collect_treasure(self):
        self.gold_coins = self.gold_coins + 1
        if self.gold_coins%10 == 0:
            self.level_up()

    def restart():
        self.gold_coins = 0
        self.health_points = 10
        self.lives= 5

    def do_battle(self, damage):
        self.health_points = self.health_points - int(damage)

        if self.health_points<1:
            if self.lives<1:
                self.restart()
            else:
                self.lives = self.lives - 1
                self.health_points = 10

player1 = player()
print(player1)

player1.level_up()
print(player1)

player1.collect_treasure()
print(player1)

player1.do_battle(12)
print(player1)
