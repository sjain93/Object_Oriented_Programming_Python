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


player1 = player()
print(player1)
