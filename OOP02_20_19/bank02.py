class BankAccount:
    interest_rate = float(1.0)
    #This is the prime interest rate
    accounts = []
    #All accounts, start as an empty list - to append to later
#These are all the class methods that operate on all accounts hollistically
    @classmethod
    def create(cls):
        new_account = cls()
        #cls here is referring the the BankAccount class as a whole, this implicitly runs the __init__ function
        cls.accounts.append(new_account)
        #reaching into our array of accounts to add new instance created in line before
        return new_account

    @classmethod
    def total_funds(cls):
        total = 0
        for account in cls.accounts:
            total += account.acc_balance
        return total

    @classmethod
    def interest_time(cls):
        for account in cls.accounts:
            account.acc_balance = account.acc_balance*(1+cls.interest_rate/100)
#Below are all the instance methods for every specific account in memory.
    def __init__(self, balance = 0):
        self.acc_balance = balance

    def deposit(self, amount):
        self.dep_amt= amount
        self.acc_balance += self.dep_amt

    def withdraw(self, amount):
        self.with_amt= amount
        self.acc_balance -= self.with_amt

#Test cases

my_account = BankAccount.create()
your_account = BankAccount.create()

print(my_account.acc_balance)
print(BankAccount.total_funds())

my_account.deposit(200)
your_account.deposit(1000)

print(my_account.acc_balance)
print(your_account.acc_balance)

print(BankAccount.total_funds())
BankAccount.interest_time()

print(my_account.acc_balance)
print(your_account.acc_balance)
print(BankAccount.total_funds())

my_account.withdraw(50)
print(my_account.acc_balance)
print(BankAccount.total_funds())
