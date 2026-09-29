BOOK_FILE = "books.txt"
MEMBER_FILE = "members.txt"

def load_books():
    books = []

    try:
        file = open(BOOK_FILE, "r")
        for line in file:
            data = line.strip().split("|")
            if len(data) == 4:
                from book import Book
                issued = data[3] == "1"
                books.append(Book(data[0], data[1], data[2], issued))
        file.close()
    except FileNotFoundError:
        pass

    return books

def save_books(books):
    file = open(BOOK_FILE, "w")
    for book in books:
        if book.issued:
            status = "1"
        else:
            status = "0"

        line = book.book_id + "|" + book.title + "|" + book.author + "|" + status + "\n"
        file.write(line)
    file.close()

def load_members():
    members = []

    try:
        file = open(MEMBER_FILE, "r")
        for line in file:
            data = line.strip().split("|")
            if len(data) >= 2:
                from member import Member

                borrowed = []
                if len(data) == 3 and data[2] != "":
                    borrowed = data[2].split(",")

                members.append(Member(data[0], data[1], borrowed))
        file.close()
    except FileNotFoundError:
        pass

    return members

def save_members(members):
    file = open(MEMBER_FILE, "w")
    for member in members:
        borrowed = ",".join(member.borrowed_books)
        line = member.member_id + "|" + member.name + "|" + borrowed + "\n"
        file.write(line)
    file.close()
