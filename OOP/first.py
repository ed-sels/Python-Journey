#Create a class called Book
class Book:

    #The init function initializes the new class with innformation
    def __init__(self, title):
        self.title = title

#Instance of a class
book_1 = Book("Lilo and Stitch")
book_2 = Book("Mulan")

#print the class
print(book_1)
print(book_1.title)