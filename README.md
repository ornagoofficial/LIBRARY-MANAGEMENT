# Library Management System

## 1. Project Overview

The **Library Management System** is a beginner-level Python command-line project for managing books and library members. It allows a user to add and search books, register members, issue and return books, and view a simple library report.

The project is designed for the VITyarthi Python project requirement and uses simple Python concepts such as functions, classes, lists, loops, conditions, file handling, and basic exception handling.

**Important:** The project does not use JSON or any external Python package. Data is stored in simple `.txt` files.

## 2. Features

- Display all books
- Add a new book
- Search books by title or author
- Register library members
- Issue a book to a member
- Return a book
- View member details
- View library statistics
- Save data using text files
- Basic validation and error handling
- Basic test file

## 3. Technologies Used

- Python 3
- Command Line Interface (CLI)
- Text file handling
- Basic Object-Oriented Programming

No external packages are required.

## 4. Project Structure

```text
Library_Management_Project/
│
├── main.py
├── library.py
├── book.py
├── member.py
├── file_manager.py
├── reports.py
├── test_library.py
├── books.txt
├── members.txt
├── README.md
└── statement.md
```

## 5. How to Run

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```text
python main.py
```

If your computer uses `python3`, run:

```text
python3 main.py
```

## 6. Testing

Run:

```text
python test_library.py
```

The program should display:

```text
All basic tests passed.
```

## 7. Data Storage

The program uses:

- `books.txt` for book information
- `members.txt` for member information

The format is simple text separated by the `|` symbol. No JSON database is used.

## 8. GitHub Upload

Create a new GitHub repository, then upload all project files. Make sure `README.md` is in the main project folder so GitHub displays it on the repository home page.

## 9. Learning Outcomes

This project demonstrates:

- Functions
- Classes and objects
- Lists
- Loops
- Conditional statements
- String operations
- File handling
- Exception handling
- Basic testing
- Modular project organization
