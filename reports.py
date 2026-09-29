def show_report(library):
    total_books = len(library.books)
    total_members = len(library.members)
    issued_books = 0
    available_books = 0

    for book in library.books:
        if book.issued:
            issued_books += 1
        else:
            available_books += 1

    print("\n===== LIBRARY REPORT =====")
    print("Total books    :", total_books)
    print("Available books:", available_books)
    print("Issued books   :", issued_books)
    print("Total members  :", total_members)
