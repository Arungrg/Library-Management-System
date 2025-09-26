library = []
users = []

from datetime import datetime, timedelta


def add_book():
    title = input("Enter the book title:")
    author = input("Enter the author name:")
    year = input("Enter the publication year:")
    status = input("Enter the status of the book (available or borrowed):").lower()

    lib = {"title": title, "author": author, "year": year, "status": status}

    library.append(lib)
    print("Book added successfully!")


def display_books():
    if not library:
        print("No books in the library")

    else:
        print("Books in the birary:")

        for books in library:
            print("Title: ", books["title"])
            print("Author: ", books["author"])
            print("Year: ", books["year"])
            print("Status", books["status"])
            print("")


def add_user():
    name = input("Enter the user name: ")
    user = {"name": name, "borrowed": []}

    users.append(user)
    print("User added successfully!")


def search_book():
    title = input("Enter the title of the book to search: ")

    for books in library:
        if books["title"] == title:
            print("Book found. Details:")
            print("Title:", books["title"])
            print("Author:", books["author"])
            print("Year:", books["year"])
            print("Status:", books["status"])
            return
    print("Book not found")


def borrow_book():
    user_name = input("Enter your name: ")
    title = input("Enter the title of the book to borrow: ")

    for user in users:
        if user["name"] == user_name:
            for books in library:
                if books["title"] == title:
                    if books["status"] == "available":
                        books["status"] = "borrowed"
                        due_date = datetime.now() + timedelta(days=7)
                        user["borrowed"].append({"title": title, "due_date": due_date})
                        print(
                            f"Book borrowed successfully! Due on {due_date.strftime('%d-%b-%Y')}"
                        )
                        return
                    else:
                        print(f"Sorry, '{title}' is already borrowed.")
                        return
            print("Book not found in the library.")
            return
    print("User not found")


def return_book():
    user_name = input("Enter your name: ")
    title = input("Enter the title of the book to return: ")

    for user in users:
        if user["name"] == user_name:
            for borrowed_book in user["borrowed"]:
                if borrowed_book["title"] == title:
                    user["borrowed"].remove(borrowed_book)
                    for books in library:
                        if books["title"] == title:
                            books["status"] = "available"

                    print("Book returned successfully!")
                    return
            print("This user did not borrow that book! ")
            return
    print("User not found")


def view_users():
    if not users:
        print("No users found.")
    for user in users:
        print("Name:", user["name"])
        if not user["borrowed"]:
            print("  No borrowed books.")
        else:
            print("  Borrowed Books:")
            for borrowed_books in user["borrowed"]:
                print(
                    f"    {borrowed_books['title']} (Due: {borrowed_books['due_date'].strftime('%d-%b-%Y')})"
                )
        print("")


def delete_book():
    title = input("Enter the title of the book to delete: ")
    for books in library:
        if books["title"] == title:
            library.remove(books)
            print("Book deleted successfully!")
            return

    print("Book not found in the library.")


def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Add User")
        print("4. Search Book")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. View Users")
        print("8. Delete Book")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            add_user()
        elif choice == "4":
            search_book()
        elif choice == "5":
            borrow_book()
        elif choice == "6":
            return_book()
        elif choice == "7":
            view_users()
        elif choice == "8":
            delete_book()
        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
