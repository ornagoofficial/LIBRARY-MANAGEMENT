class Book:
    def __init__(self, book_id, title, author, issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = issued

    def issue(self):
        self.issued = True

    def return_book(self):
        self.issued = False

    def display(self):
        if self.issued:
            status = "Issued"
        else:
            status = "Available"

        return self.book_id + " | " + self.title + " | " + self.author + " | " + status
