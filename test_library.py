from book import Book
from member import Member

def test_book():
    book = Book("B01", "Python Basics", "John")
    assert book.issued == False
    book.issue()
    assert book.issued == True
    book.return_book()
    assert book.issued == False

def test_member():
    member = Member("M01", "Student")
    member.borrow_book("B01")
    assert "B01" in member.borrowed_books
    member.return_book("B01")
    assert "B01" not in member.borrowed_books

def test_book_display():
    book = Book("B02", "Math", "Author")
    result = book.display()
    assert "Math" in result

test_book()
test_member()
test_book_display()
print("All basic tests passed.")
