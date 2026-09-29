from library import Library
from reports import show_report

def show_menu():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Show all books")
    print("2. Add book")
    print("3. Search book")
    print("4. Register member")
    print("5. Issue book")
    print("6. Return book")
    print("7. Show member details")
    print("8. Show library report")
    print("9. Exit")

def get_number(message):
    try:
        return int(input(message))
    except ValueError:
        print("Please enter a valid number.")
        return -1

def main():
    library = Library()

    while True:
        show_menu()
        choice = get_number("Enter your choice: ")

        if choice == 1:
            library.show_books()

        elif choice == 2:
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(book_id, title, author)

        elif choice == 3:
            keyword = input("Enter title or author to search: ")
            library.search_book(keyword)

        elif choice == 4:
            member_id = input("Enter member ID: ")
            name = input("Enter member name: ")
            library.add_member(member_id, name)

        elif choice == 5:
            book_id = input("Enter book ID: ")
            member_id = input("Enter member ID: ")
            library.issue_book(book_id, member_id)

        elif choice == 6:
            book_id = input("Enter book ID: ")
            member_id = input("Enter member ID: ")
            library.return_book(book_id, member_id)

        elif choice == 7:
            member_id = input("Enter member ID: ")
            library.show_member(member_id)

        elif choice == 8:
            show_report(library)

        elif choice == 9:
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please select 1 to 9.")

if __name__ == "__main__":
    main()
