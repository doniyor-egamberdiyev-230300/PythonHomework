class BookNotFoundException(Exception):
    pass


class BookAlreadyBorrowedException(Exception):
    pass


class MemberLimitExceededException(Exception):
    pass


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} ({status})"


class Member:
    MAX_BORROWED_BOOKS = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= Member.MAX_BORROWED_BOOKS:
            raise MemberLimitExceededException(
                f"{self.name} cannot borrow more than {Member.MAX_BORROWED_BOOKS} books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} is already borrowed.")

        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
        else:
            raise BookNotFoundException(f"{self.name} has not borrowed {book.title}.")

    def __str__(self):
        books = ', '.join([book.title for book in self.borrowed_books]) or "No books borrowed"
        return f"Member: {self.name}, Borrowed Books: {books}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise BookNotFoundException(f"Book '{title}' not found in the library.")

    def borrow_book(self, member, title):
        book = self.find_book(title)
        member.borrow_book(book)

    def return_book(self, member, title):
        book = self.find_book(title)
        member.return_book(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def display_members(self):
        for member in self.members:
            print(member)


# Test cases
library = Library()

# Adding books
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Adding members
member1 = Member("Alice")
member2 = Member("Bob")
library.add_member(member1)
library.add_member(member2)

# Borrowing books
try:
    library.borrow_book(member1, "1984")
    library.borrow_book(member1, "To Kill a Mockingbird")
    library.borrow_book(member1, "The Great Gatsby")
    # Attempt to borrow a fourth book (should raise exception)
    library.borrow_book(member1, "Unknown Book")
except Exception as e:
    print(e)

# Returning a book
try:
    library.return_book(member1, "1984")
except Exception as e:
    print(e)

# Display books and members
library.display_books()
library.display_members()