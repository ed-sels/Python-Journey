#Create a class called Book
class Book:

    # This attribute has a scope of the class Book
    BOOK_TYPES = ("Hard Cover", "Paper Back", "Ebook")
    #The init function initializes the new class with innformation
    def __init__(self, title, author, pages, price, booktype):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type.")
        else:
            self.booktype = booktype

    #function to get price of a book
    def getPrice(self):
        # "hasattr" function checks to see if an attribute exists
        # the _ sign used before the discount indicates that it is only intended to be used by the class.
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
        
    
    def setDiscount(self, amount):
        self._discount = amount


#Instance of a class
book_1 = Book("Alex Rider", "Anthony Horowitz", 204, 59.99, "Hard Cover")
book_2 = Book("Narnia", "C.S. Lewis", 320, 79.99, "Comic")


#print the class
print(book_1)
print(book_1.title)

#print price of book
print(book_1.getPrice())
book_1.setDiscount(0.2)
print(book_1.getPrice())

#using the isinstance function to compare a specific instance to a known type
print(isinstance(book_1,Book))
print(isinstance(book_1,object))