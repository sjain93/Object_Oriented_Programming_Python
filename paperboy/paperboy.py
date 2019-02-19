class paperboy:
    """ A class representing a paperboy"""

    def __init__(self, name, experience, earnings):
        self.name = str(name)
        self.exp = float(experience)
        self.earnings= float(earnings)
        self.quota = None

    def __str__(self):
        return "PaperBoy name:{}\nPaperBoy Experience:{}\nPaperBoy earnings:{}".format(self.name, self.exp, self.earnings)

    def calculate_quota(self):
        self.quota = float(50+ (self.exp/2))

    def deliver(self, start_address, end_address):
        self.start_address = int(start_address)
        self.end_address = int(end_address)
        self.papers_delivered = abs(self.end_address-self.start_address)
        self.exp = self.papers_delivered
        self.calculate_quota()
        if self.papers_delivered < self.quota:
            self.earnings = float(self.papers_delivered*0.25 - 2)
        elif self.papers_delivered == self.quota:
            self.earnings = float(self.papers_delivered*0.25)
        else:
            self.earnings = float(self.quota*0.25 + (self.papers_delivered-self.quota*0.5))

        return self.earnings

    def report(self):
        return "My name is {}, I've delivered {} papers and earned ${} so far!".format(self.name, self.papers_delivered, self.earnings)


tommy = paperboy("Tommy", 0, 0)
import pry;
pry()

print(tommy)
# print(tommy.quota())
print(tommy.deliver(101, 160))

print(tommy.report())
# tommy.report()
