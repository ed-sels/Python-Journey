class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Member(Person):
    def __init__(self, name, id, membership_type):
        super().__init__(name, id)
        self.membership_type = membership_type

    def books_borrowed(self, list):
        return f"{self.name} has borrowed books under {self.membership_type} membership."

    def borrow_book(self, book_title):
        return f"{self.name} has borrowed the book: {book_title}."
    
    def list_books(self, books):
        return f"{self.name} has the following books: {', '.join(books)}."
    
member1 = Member("Alice", 101, "Gold")
member2 = Member("Kofi", 102, "Platinum")

# Members borrow books
print(member1.borrow_book("Python Programming"))
print(member2.borrow_book("Data Engineering 101"))

# Members list their borrowed books
print(member1.list_books(["Python Programming", "Machine Learning"]))