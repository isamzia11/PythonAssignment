# Name Isam Zia Roll no: TRN-2026-00346 

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} - {status}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return (
            f"{super().__str__()} "
            f"({self.file_size} MB)"
        )


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print("Book borrowed successfully")
                else:
                    print("Book is already borrowed")
                return

        print("Book not found")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print("Book returned")
                return

        print("Book not found")

    def available_books(self):
        return [book for book in self.books if book.available]


library = Library()

library.add_book(Book("Python Basics", "Ali"))
library.add_book(Book("Data Science", "Sara"))
library.add_book(EBook("AI Guide", "Ahmed", 12.5))

print("===== AVAILABLE BOOKS =====")
for book in library.available_books():
    print(book)

library.borrow("Python Basics")

print("\n===== AFTER BORROWING =====")
for book in library.available_books():
    print(book)

library.return_book("Python Basics")
