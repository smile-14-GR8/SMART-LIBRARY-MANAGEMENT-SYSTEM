# ==========================================
# SMART LIBRARY MANAGEMENT SYSTEM
# ==========================================

books = [
    {
        "id": 101,
        "title": "Python Programming",
        "author": "John Zelle",
        "category": "Computer Science",
        "available": True
    },

    {
        "id": 102,
        "title": "Learning Python",
        "author": "Mark Lutz",
        "category": "Computer Science",
        "available": True
    },

    {
        "id": 103,
        "title": "Data Structures",
        "author": "Seymour Lipschutz",
        "category": "Computer Science",
        "available": True
    },

    {
        "id": 104,
        "title": "Engineering Mathematics",
        "author": "B. S. Grewal",
        "category": "Mathematics",
        "available": True
    },

    {
        "id": 105,
        "title": "Concepts of Physics",
        "author": "H. C. Verma",
        "category": "Physics",
        "available": True
    },

    {
        "id": 106,
        "title": "Atomic Habits",
        "author": "James Clear",
        "category": "Self Improvement",
        "available": True
    }
]


students = {}

borrowed_books = []


# ==========================================
# DISPLAY BOOKS
# ==========================================

def display_books():

    print("\n")
    print("=" * 80)
    print("                         BOOK LIST")
    print("=" * 80)

    print("ID\tTitle\t\t\tAuthor\t\t\tStatus")
    print("-" * 80)

    for book in books:
        if book["available"] == True:
            status = "Available"
        else:
            status = "Issued"
        print(
            book["id"],
            "\t",
            book["title"],
            "\t",
            book["author"],
            "\t",
            status
        )
    print("=" * 80)


# ==========================================
# REGISTER STUDENT
# ==========================================

def register_student():

    print("\n")
    print("=" * 50)
    print("             STUDENT REGISTRATION")
    print("=" * 50)

    name = input("Enter Student Name: ")
    registration_no = input("Enter Registration Number: ")

    if registration_no in students:
        print("\nStudent already registered!")
        return None
    students[registration_no] = name
    print("\nRegistration Successful!")
    print("Welcome", name)
    return registration_no


# ==========================================
# SEARCH BOOK
# ==========================================

def search_book():

    print("\n===== SEARCH BOOK =====")
    keyword = input(
        "Enter book title or author: "
    )
    found = False
    for book in books:

        if (
            keyword.lower() in book["title"].lower()
            or
            keyword.lower() in book["author"].lower()
        ):
            print("\nBook Found!")
            print("Book ID:", book["id"])
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Category:", book["category"])
            if book["available"]:
                print("Status: Available")
            else:
                print("Status: Issued")
            found = True
    if found == False:
        print("\nNo book found.")


# ==========================================
# ISSUE BOOK
# ==========================================

def issue_book(registration_no):
    print("\n===== ISSUE BOOK =====")
    display_books()
    try:
        book_id = int(
            input("\nEnter Book ID: ")
        )
    except:
        print("Please enter a valid Book ID.")
        return
    found = False
    for book in books:
        if book["id"] == book_id:
            found = True
            if book["available"] == True:
                already_borrowed = False
                for item in borrowed_books:
                    if (
                        item[0] == registration_no
                        and
                        item[1] == book_id
                    ):
                        already_borrowed = True
                if already_borrowed:
                    print(
                        "\nYou already have this book."
                    )
                    return
                book["available"] = False
                borrowed_books.append(
                    [registration_no, book_id]
                )
                print("\nBook issued successfully!")
                print("Book:", book["title"])
            else:
                print(
                    "\nSorry, this book is already issued."
                )
    if found == False:
        print("\nBook not found.")


# ==========================================
# RETURN BOOK
# ==========================================

def return_book(registration_no):
    print("\n===== RETURN BOOK =====")
    try:
        book_id = int(
            input("Enter Book ID: ")
        )
    except:
        print("Please enter a valid Book ID.")
        return
    found = False
    for item in borrowed_books:
        if (
            item[0] == registration_no
            and
            item[1] == book_id
        ):
            found = True
            borrowed_books.remove(item)
            for book in books:
                if book["id"] == book_id:
                    book["available"] = True
                    print("\nBook returned successfully!")
                    print("Book:", book["title"])

                    return
    if found == False:
        print(
            "\nYou have not borrowed this book."
        )


# ==========================================
# MY BORROWED BOOKS
# ==========================================

def my_books(registration_no):

    print("\n===== MY BORROWED BOOKS =====")
    found = False
    for item in borrowed_books:
        if item[0] == registration_no:
            found = True
            book_id = item[1]
            for book in books:
                if book["id"] == book_id:
                    print("\nBook ID:", book["id"])
                    print("Title:", book["title"])
                    print("Author:", book["author"])
                    print("Category:", book["category"])

    if found == False:
        print("\nYou have no borrowed books.")


# ==========================================
# ADD BOOK
# ==========================================

def add_book():
    print("\n===== ADD NEW BOOK =====")
    try:
        book_id = int(
            input("Enter Book ID: ")
        )
    except:
        print("Invalid Book ID.")
        return
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    category = input("Enter Category: ")
    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "category": category,
        "available": True
    }
    books.append(new_book)
    print("\nBook added successfully!")


# ==========================================
# REMOVE BOOK
# ==========================================

def remove_book():
    print("\n===== REMOVE BOOK =====")
    try:
        book_id = int(
            input("Enter Book ID: ")
        )
    except:
        print("Invalid Book ID.")
        return
    for book in books:
        if book["id"] == book_id:
            if book["available"] == True:
                books.remove(book)
                print("\nBook removed successfully!")
            else:
                print(
                    "\nCannot remove an issued book."
                )
            return
    print("\nBook not found.")


# ==========================================
# VIEW STUDENTS
# ==========================================

def view_students():
    print("\n===== REGISTERED STUDENTS =====")
    if len(students) == 0:
        print("No students registered.")
        return
    for registration_no in students:
        print(
            "Registration No.:",
            registration_no,
            "| Name:",
            students[registration_no]
        )


# ==========================================
# VIEW ISSUED BOOKS
# ==========================================

def view_issued_books():
    print("\n===== ISSUED BOOKS =====")
    if len(borrowed_books) == 0:
        print("No books are currently issued.")
        return
    for item in borrowed_books:
        registration_no = item[0]
        book_id = item[1]

        print(
            "Student:",
            students[registration_no],
            "| Registration No.:",
            registration_no,
            "| Book ID:",
            book_id
        )


# ==========================================
# STUDENT MENU
# ==========================================

def student_menu(registration_no):

    while True:
        print("\n")
        print("=" * 50)
        print("              STUDENT MENU")
        print("=" * 50)

        print(
            "Welcome,",
            students[registration_no]
        )
        print("\n1. View Books")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. My Borrowed Books")
        print("6. Exit")

        choice = input(
            "\nEnter your choice: "
        )
        if choice == "1":
            display_books()
        elif choice == "2":
            search_book()
        elif choice == "3":
            issue_book(registration_no)
        elif choice == "4":
            return_book(registration_no)
        elif choice == "5":
            my_books(registration_no)
        elif choice == "6":
            print("\nExiting Student Menu...")
            break
        else:
            print("\nInvalid choice!")


# ==========================================
# LIBRARIAN MENU
# ==========================================

def librarian_menu():

    while True:

        print("\n")
        print("=" * 50)
        print("             LIBRARIAN MENU")
        print("=" * 50)

        print("1. View All Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. View Students")
        print("5. View Issued Books")
        print("6. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            display_books()

        elif choice == "2":

            add_book()

        elif choice == "3":

            remove_book()

        elif choice == "4":

            view_students()

        elif choice == "5":

            view_issued_books()

        elif choice == "6":

            print("\nExiting Librarian Menu...")

            break

        else:

            print("\nInvalid choice!")


# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        print("\n")
        print("=" * 60)
        print("          SMART LIBRARY MANAGEMENT SYSTEM")
        print("=" * 60)

        print("\n1. Register Student")
        print("2. Student Login")
        print("3. Librarian Menu")
        print("4. View Books")
        print("5. Exit")

        choice = input(
            "\nEnter your choice: "
        )

        # REGISTER STUDENT
        if choice == "1":
            registration_no = register_student()
            if registration_no != None:
                student_menu(registration_no)

        # STUDENT LOGIN
        elif choice == "2":
            registration_no = input(
                "Enter Registration Number: "
            )
            if registration_no in students:
                student_menu(registration_no)
            else:
                print(
                    "\nStudent not registered!"
                )

        # LIBRARIAN MENU
        elif choice == "3":

            librarian_menu()

        # VIEW BOOKS
        elif choice == "4":

            display_books()

        # EXIT
        elif choice == "5":
            print(
                "\nThank you for using Smart Library!"
            )
            break
        else:
            print("\nInvalid choice!")


# ==========================================
# START PROGRAM
# ==========================================

main()
