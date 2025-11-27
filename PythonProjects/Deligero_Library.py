library = []

def add():
    try:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")

        book = {
            "Title" : title,
            "Author" : author,
            "Year" : year,
            }
    
        library.append(book)
        print('\nBook added successfully.\n')
    
    except Exception as e:
        print(f"An error occurred: {e}")

def remove():
    try:
        to_remove = input('Enter the title of the book to remove: ')
        for book in library:
            if book['Title'].lower() == to_remove.lower():
                library.remove(book)
                print('\nBook removed successfully\n')
                return
    except Exception as e:  
        print(f"An error occurred: {e}")

def search():
    try:
            author_name = input("\nEnter author name to search: ")
            book_found = [book for book in library if book['Author'].lower() == author_name.lower()]
            if not book_found:
                print(f"\nNo books found by author: {author_name}\n")
            else:
                print(f"\nBooks by {author_name}:")
                for i, book in enumerate(book_found, start=1):
                    print(f"{i}. {book['Title']} ({book['Year']})")
                print(' ')
    except Exception as e:
        print(f"An error occurred: {e}")
            
def display():
    try:
        if library:
            print("\nList of all books:")
            for i, book in enumerate(library, start=1):
                print(f"{i}. {book['Title']} by {book['Author']} ({book['Year']})")
            print(' ')
        else:
            print("\nNo books in the library.\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def menu():
    try:
        while True:
            print('[1] Add Book')
            print('[2] Remove Book')
            print('[3] Search Book')
            print('[4] Display All Books')
            print('[5] Exit')
            opt = input('Option: ')

            if opt == '1':
                add()

            elif opt == '2':
                remove()
        
            elif opt == '3':        
                search()
        
            elif opt == '4':
                display()
        
            elif opt == '5':
                print('\nThank you for using the program.\n')
                break
        
            else:
                print('Invalid option. Please try again.')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    menu()