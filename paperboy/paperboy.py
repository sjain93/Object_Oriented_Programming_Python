class paperboy:
    """ A class representing a paperboy"""
    min_papers = 50

    def __init__(self, name, experience, earnings):
        self.name = str(name)
        self.exp = float(experience)
        self.earnings= float(earnings)

    def __str__(self):
        return "PaperBoy name:{}\nPaperBoy Experience:{}\nPaperBoy earnings:{}".format(self.name, self.exp, self.earnings)

    def quota(self):
        self.quot = float(min_papers + (self.exp/2))
        return self.quot

    def deliver(self, start_address, end_address):
        self.start_address = int(start_address)
        self.end_address = int(end_address)
        self.papers_delivered = abs(self.end_address-self.start_address)
        self.exp = self.papers_delivered

        if self.papers_delivered < quota.self.quot:
            self.earnings = float(self.papers_delivered*0.25 - 2)
        elif self.papers_delivered == self.quot:
            self.earnings = float(self.papers_delivered*0.25)
        else:
            self.earnings = float(self.quot*0.25 + (self.papers_delivered-self.quot)*0.5)

        return self.earnings

    def report(self):
        return "My name is {}, I've delivered {} papers and earned {} so far!".format(self.name, self.papers_delivered, self.earnings)


tommy = paperboy("Tommy", 0, 0)
print(tommy)

tommy.deliver(101, 160)
print(tommy.earnings)
tommy.report()
