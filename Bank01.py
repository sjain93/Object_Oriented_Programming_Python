class BankAccount:
    """Class representing a bank account """

    def __init__(self, fname, lname, balance = 0, interest = 0):
        self.first_name = fname
        self.last_name = lname
        self.balance = balance
        self.interest_rate = interest

    def __str__(self):
        return "Bank Account holder: {} {}\nCurrent balance is ${}, Interest rate is {}%".format(self.first_name, self.last_name, self.balance, self.interest_rate)

    def deposit(self, amount):
        self.added_amount = amount
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.removed_amount = amount
        self.balance = self.balance - amount


TestAcc = BankAccount("Sanchit", "Jain", 20, 0)
TestAcc.interest_rate = 1.64

print(TestAcc)

TestAcc.deposit(20)

print(TestAcc)

TestAcc.withdraw(5)

print(TestAcc)
