class Library:

    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    def check_out(self):
        if self.available:
            self.available = False
            print(self.book_name, "by", self.author, "has been checked out")
        else:
            print(self.book_name, "is not available")

    def return_book(self):
        if not self.available:
            self.available = True
            print(self.book_name, "has been returned")
        else:
            print(self.book_name, "was not checked out")

    def display_status(self):
        if self.available:
            print(self.book_name, "by", self.author, "- Available")
        else:
            print(self.book_name, "by", self.author, "- Checked out")


books = [
    Library("1984", "George Orwell"),
    Library("To Kill a Mockingbird", "Harper Lee"),
    Library("The Great Gatsby", "F. Scott Fitzgerald")
]


while True:

    print("\n1. Display Books")
    print("2. Check Out Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for book in books:
            book.display_status()

    elif choice == "2":
        name = input("Enter book name: ")
        for book in books:
            if book.book_name.lower() == name.lower():
                book.check_out()
                break
        else:
            print("Book not found")

    elif choice == "3":
        name = input("Enter book name: ")
        for book in books:
            if book.book_name.lower() == name.lower():
                book.return_book()
                break
        else:
            print("Book not found")

    elif choice == "4":
        print("Exiting Library")
        break

    else:
        print("Invalid choice")