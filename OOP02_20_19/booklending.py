from datetime import datetime
import random

class Book:
    on_shelf = []
    on_loan = []
    overdue = []

    @classmethod
    def create(cls, title, author, ISBN):
        new_book = Book(title, author, ISBN)
        Book.on_shelf.append(new_book)
        return new_book

    @classmethod
    def browse(cls):
        return random.choice(cls.on_shelf)

    @classmethod
    def current_due_date(cls):
        now = datetime.now()
        two_weeks = 60*60*24*14
        future_timestamp = now.timestamp() + two_weeks
        return datetime.fromtimestamp(future_timestamp)

    @classmethod
    def overdue(cls):
        for books in Book.on_loan:
            if books.due_date < datetime.now():
                Book.overdue.append(books)
        return Book.overdue

    def borrow(self):
        if self.lent_out() == True:
            return False
        else:
            self.due_date = Book.current_due_date()
            book_index = Book.on_shelf.index(self)
            Book.on_shelf.pop(book_index)
            Book.on_loan.append(self)

    def return_to_library(self):
        if self.lent_out() == False:
            return False
        else:
            book_index = Book.on_loan.index(self)
            Book.on_loan.pop(book_index)
            Book.on_shelf.append(self)
            self.due_date = None

    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.due_date = None

    def lent_out(self):
        if self in Book.on_loan:
            return True
        else:
            return False


sister_outsider = Book.create("Sister Outsider", "Audre Lorde", "9781515905431")
aint_i = Book.create("Ain't I a Woman?", "Bell Hooks", "9780896081307")
if_they_come = Book.create("If They Come in the Morning", "Angela Y. Davis", "0893880221")

print(Book.browse().title)
print(sister_outsider.lent_out())

print(Book.on_loan)
sister_outsider.borrow()
print(Book.on_loan[0].title)
print(sister_outsider.due_date)
print(aint_i.lent_out())
sister_outsider.return_to_library()
print(Book.on_loan)
print(Book.on_shelf)
print(len(Book.overdue()))
