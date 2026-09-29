# VITyarthi Smart Library Management System

A simple CLI-based library management project developed in Python. The
system simulates common library operations such as student registration,
book searching, issuing and returning books, and librarian-side book and
student management.

## Overview of the Project

The **Smart Library Management System** was created to apply Python
programming concepts to a real-world problem. The project provides a
logical workflow for students and librarians through a command-line
interface.

The current implementation uses Python lists and dictionaries to manage
books, students, and borrowed-book records during program execution. No
external database or third-party library is required.

## Problem Being Addressed

Managing library records manually can make it difficult to keep track of
available books, issued books, student records, and book returns.

This project provides a simple digital system that organizes these
operations through an interactive Python CLI.

## Target Users

-   Students who want to search, issue, return, and view borrowed books
-   Librarians who need to manage books and view student and issue
    records

## Features

### Student Module

-   Student registration
-   Student login using registration number
-   View all books
-   Search books by title or author
-   Issue available books
-   Return borrowed books
-   View currently borrowed books

### Librarian Module

-   View all books
-   Add new books
-   Remove available books
-   View registered students
-   View currently issued books

### Book Management Module

-   Store book ID, title, author, category, and availability
-   Search book information
-   Change book status when issued or returned
-   Add and remove books

## Functional Requirements

The system provides the following major functional modules:

1.  **Student Management** -- registration and login using a
    registration number.
2.  **Book Management** -- viewing, searching, adding, and removing
    books.
3.  **Transaction Management** -- issuing and returning books and
    tracking borrowed books.
4.  **Librarian Management** -- viewing student and issued-book
    information.

## Non-Functional Requirements

-   **Usability:** The CLI menus are simple and easy to navigate.
-   **Reliability:** The system checks student registration, book
    availability, and borrowing records before performing operations.
-   **Error Handling:** Invalid numeric inputs and unavailable books are
    handled with appropriate messages.
-   **Maintainability:** The project is organized into separate
    functions for individual operations, making the code easier to
    understand and modify.
-   **Resource Efficiency:** The system uses lightweight Python data
    structures and does not require external libraries or a database.

## Technologies / Tools Used

-   Python
-   Python IDLE / VS Code
-   Lists
-   Dictionaries
-   Functions
-   Loops
-   Conditional statements
-   Git and GitHub for version control

## Project Structure

``` text
SMART-LIBRARY-MANAGEMENT-SYSTEM/
│
├── main.py
├── README.md
└── statement.md
```

> Note: The VITyarthi project guidelines specify a modular
> implementation with 5--10 meaningful modules/classes/files for coding
> projects. The current prototype is implemented in one Python file and
> can be modularized further if required by the course evaluation.

## Steps to Install & Run the Project

### 1. Install Python

Make sure Python 3 is installed on your computer.

### 2. Download or Clone the Repository

Download the project files or clone the GitHub repository.

### 3. Run the Project

Open the Python file in IDLE or VS Code.

You can also run it from the terminal:

``` bash
python main.py
```

If the filename contains spaces, use:

``` bash
python "SMART LIBRARY MANAGEMENT SYSTEM.py"
```

## Instructions for Testing and How to Use It

### Create an Account

1.  Start the program.
2.  Select **Register Student**.
3.  Enter the student's name.
4.  Enter the registration number.
5.  After successful registration, the Student Menu opens automatically.

### Student Login

1.  Select **Student Login**.
2.  Enter the registration number used during registration.
3.  Access the Student Menu.

### Student Operations

The Student Menu provides:

``` text
1. View Books
2. Search Book
3. Issue Book
4. Return Book
5. My Borrowed Books
6. Exit
```

### Book Operations

-   **View Books:** Displays all books and their availability.
-   **Search Book:** Searches using a book title or author's name.
-   **Issue Book:** Issues an available book using its Book ID.
-   **Return Book:** Returns a book previously borrowed by the student.
-   **My Borrowed Books:** Displays books currently borrowed by the
    logged-in student.

### Librarian Operations

The Librarian Menu provides:

``` text
1. View All Books
2. Add Book
3. Remove Book
4. View Students
5. View Issued Books
6. Exit
```

## Sample Books

The project initially contains:

  Book ID   Title                     Author              Category
  --------- ------------------------- ------------------- ------------------
  101       Python Programming        John Zelle          Computer Science
  102       Learning Python           Mark Lutz           Computer Science
  103       Data Structures           Seymour Lipschutz   Computer Science
  104       Engineering Mathematics   B. S. Grewal        Mathematics
  105       Concepts of Physics       H. C. Verma         Physics
  106       Atomic Habits             James Clear         Self Improvement

## Testing Approach

The system can be tested using the following scenarios:

  Test Case                                   Expected Result
  ------------------------------------------- -------------------------------------
  Register a new student                      Student is registered successfully
  Register an existing registration number    Registration is rejected
  Login with a registered student             Student menu opens
  Login with an unregistered student          Error message is displayed
  Search for an existing book                 Book details are displayed
  Search for a non-existing book              No book found message
  Issue an available book                     Book status changes to Issued
  Issue an already issued book                Issue is rejected
  Return a borrowed book                      Book status changes to Available
  Return a book not borrowed by the student   Return is rejected
  Add a new book                              Book is added to the library
  Remove an available book                    Book is removed
  View issued books                           Current issue records are displayed

## Limitations

-   Data is stored only while the program is running.
-   No external database or file-based persistence is used.
-   The librarian section does not currently use password
    authentication.
-   The current implementation is a single-file CLI prototype and can be
    further modularized.

## Future Enhancements

-   Add a database for permanent storage.
-   Add librarian authentication.
-   Add due dates and automatic fine calculation.
-   Add book reservation functionality.
-   Add a graphical user interface.
-   Add more detailed reports and analytics.
-   Modularize the project into multiple Python files/classes.
-   Add automated unit tests.

## Design and Documentation

For the complete VITyarthi submission, the project can be documented
with:

-   Problem Statement
-   Objectives
-   Functional Requirements
-   Non-Functional Requirements
-   System Architecture Diagram
-   Workflow Diagram
-   Use Case Diagram
-   Class/Component Diagram
-   Sequence Diagram
-   Testing Results
-   Screenshots
-   Challenges and Learnings
-   Future Enhancements

## Author

**Made by:** Smile Ray

**Registration Number:** 26BCE10298

## Project Information

**Project Title:** VITyarthi Smart Library Management System

**Project Type:** Python / CLI Application

**Course:** VITyarthi - Build Your Own Project

------------------------------------------------------------------------

*Developed as an educational project to demonstrate Python programming
concepts through a practical library management application.*
