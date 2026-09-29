from book import Book
from member import Member
from file_manager import load_books, save_books, load_members, save_members

class Library:
    def __init__(self):
        self.books = load_books()
        self.members = load_members()

    def add_book(self, book_id, title, author):
        for book in self.books:
            if book.book_id == book_id:
                print("A book with this ID already exists.")
                return

        book = Book(book_id, title, author)
        self.books.append(book)
        save_books(self.books)
        print("Book added successfully.")

    def show_books(self):
        if len(self.books) == 0:
            print("No books are available.")
            return

        print("\n--- Book List ---")
        for book in self.books:
            print(book.display())

    def search_book(self, keyword):
        found = False
        keyword = keyword.lower()

        for book in self.books:
            if keyword in book.title.lower() or keyword in book.author.lower():
                print(book.display())
                found = True

        if not found:
            print("No matching book found.")

    def add_member(self, member_id, name):
        for member in self.members:
            if member.member_id == member_id:
                print("A member with this ID already exists.")
                return

        member = Member(member_id, name)
        self.members.append(member)
        save_members(self.members)
        print("Member registered successfully.")

    def issue_book(self, book_id, member_id):
        selected_book = None
        selected_member = None

        for book in self.books:
            if book.book_id == book_id:
                selected_book = book

        for member in self.members:
            if member.member_id == member_id:
                selected_member = member

        if selected_book is None:
            print("Book not found.")
            return

        if selected_member is None:
            print("Member not found.")
            return

        if selected_book.issued:
            print("This book is already issued.")
            return

        selected_book.issue()
        selected_member.borrow_book(book_id)
        save_books(self.books)
        save_members(self.members)
        print("Book issued successfully.")

    def return_book(self, book_id, member_id):
        selected_book = None
        selected_member = None

        for book in self.books:
            if book.book_id == book_id:
                selected_book = book

        for member in self.members:
            if member.member_id == member_id:
                selected_member = member

        if selected_book is None:
            print("Book not found.")
            return

        if selected_member is None:
            print("Member not found.")
            return

        if not selected_book.issued:
            print("This book is already available.")
            return

        selected_book.return_book()
        selected_member.return_book(book_id)
        save_books(self.books)
        save_members(self.members)
        print("Book returned successfully.")

    def show_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                print(member.display())
                return
        print("Member not found.")
