library = []
book_id = 1

def add_book():

    global book_id

    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")

    book = {
        "ID": book_id,
        "Title": title,
        "Author": author,
        "Year": year
    }

    library.append(book)
    book_id += 1

    print(f"\nBook '{title}' by {author} added to the library.")

def remove_book():

    title = input("Enter the title of the book to remove: ")

    for book in library:
        if book['Title'].lower() == title.lower():
            library.remove(book)
            
            print(f"\nBook '{title}' has been removed from the library.")

            return
        
    print(f"\nBook '{title}' not found in the library.")

def search_books():
    mode = input("Search by 1=Author or 2=Title: ")
    if mode == "1":
        name = input("Enter author name: ")
        found = [b for b in library if b['Author'].lower() == name.lower()]
        if not found:
            print(f"\nNo books found by author: {name}")
        else:
            print(f"\nBooks by {name}:")
            for i, b in enumerate(found, start=1):
                print(f"{i}. {b['Title']} ({b['Year']}) ID {b['ID']}")
    elif mode == "2":
        name = input("Enter title: ")
        found = [b for b in library if name.lower() in b['Title'].lower()]
        if not found:
            print(f"\nNo matching titles found for: {name}")
        else:
            print("\nMatching titles:")
            for i, b in enumerate(found, start=1):
                print(f"{i}. {b['Title']} by {b['Author']} ({b['Year']}) ID {b['ID']}")
    else:
        print("\nInvalid option.")

def display_all_books():
    if not library:
        print("\nNo books in the library.")
        return
    sorted_books = sorted(library, key=lambda b: b["Title"].lower())
    print("\nList of all books:")
    for i, b in enumerate(sorted_books, start=1):
        print(f"{i}. {b['Title']} by {b['Author']} ({b['Year']}) ID {b['ID']}")

def main():
    global library, book_id
    while True:
        print("\n====== LIBRARY MENU ======")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search a Book")
        print("4. Display All Books")
        print("5. Exit")

        option = input("Choose an option: ")

        if option == "1":
            add_book()
        elif option == "2":
            remove_book()
        elif option == "3":
            search_books()
        elif option == "4":
            display_all_books()
        elif option == "5":
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
