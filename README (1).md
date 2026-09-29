# Project Title- VITyarthi Smart Library Management System

A simple CLI based library management project, developed in Python. This
project implements basic library operations such as student
registration, book searching, issuing and returning books, and librarian
management.

## Overview of the project

This project was created to understand how Python programming concepts
can be used to solve a real-world library management problem.

The system uses Python lists and dictionaries to store information about
students, books, and borrowed books while the program is running. It
provides separate options for students and librarians through a simple
command-line interface.

## Features

-   Student registration using name and registration number
-   Student login using registration number
-   View all books and their availability
-   Search books by title or author
-   Issue an available book
-   Return a borrowed book
-   View currently borrowed books
-   Add new books
-   Remove available books
-   View registered students
-   View currently issued books
-   Simple command-line interface

## Technologies/tools used

-   Python
-   Python IDLE / VS Code
-   Lists
-   Dictionaries
-   Functions
-   Loops
-   Conditional statements

## Steps to install & run the project

-   Ensure you have Python installed
-   Download or clone the GitHub repository
-   Open the Python file in IDLE, VS Code, or another Python editor
-   Run the `main.py` file

If the file is named `SMART LIBRARY MANAGEMENT SYSTEM.py`, run:

``` bash
python "SMART LIBRARY MANAGEMENT SYSTEM.py"
```

## Instructions for testing and How to use it

### Register a student

-   Choose the **Register Student** option
-   Enter the student's name
-   Enter the registration number
-   After successful registration, the Student Menu opens automatically

### Student Login

-   Choose the **Student Login** option
-   Enter the registration number used during registration
-   The Student Menu will open after successful login

### Student actions

-   **View Books:** Display all books and their availability
-   **Search Book:** Search for a book using its title or author's name
-   **Issue Book:** Enter the Book ID to issue an available book
-   **Return Book:** Enter the Book ID to return a borrowed book
-   **My Borrowed Books:** View books currently borrowed by the student

### Librarian actions

-   **View All Books:** Display the complete book list
-   **Add Book:** Add a new book using its ID, title, author, and
    category
-   **Remove Book:** Remove an available book
-   **View Students:** Display registered students
-   **View Issued Books:** Display currently issued books

## Sample books included

-   Python Programming
-   Learning Python
-   Data Structures
-   Engineering Mathematics
-   Concepts of Physics
-   Atomic Habits

## Project limitations

-   Data is stored only while the program is running
-   No external database or file storage is used
-   Librarian authentication is not included in the current version

## Author

Made by: Smile Ray

Registration Number: 26BCE10298
