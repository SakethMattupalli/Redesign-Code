from models import Library, Book, User
from storage import Storage
import utils

def main():
    storage = Storage('books.json', 'users.json')
    library = Library()
    
    library.books = storage.load_books()
    library.users = storage.load_users()

    while True:
        utils.print_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            copies = int(input("Enter number of copies: "))
            library.add_book(Book(title, author, isbn, copies))
            storage.save_books(library.list_books())

        elif choice == '2':
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new title (leave blank to keep current): ")
            author = input("Enter new author (leave blank to keep current): ")
            copies = input("Enter new number of copies (leave blank to keep current): ")
            copies = int(copies) if copies else None
            library.update_book(isbn, title or None, author or None, copies)
            storage.save_books(library.list_books())

        elif choice == '3':
            isbn = input("Enter ISBN of the book to delete: ")
            library.delete_book(isbn)
            storage.save_books(library.list_books())

        elif choice == '4':
            utils.print_books(library.list_books())

        elif choice == '5':
            title = input("Enter title to search: ")
            author = input("Enter author to search: ")
            isbn = input("Enter ISBN to search: ")
            results = library.search_books(title or None, author or None, isbn or None)
            utils.print_books(results)

        elif choice == '6':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            library.add_user(User(name, user_id))
            storage.save_users(library.list_users())

        elif choice == '7':
            user_id = input("Enter user ID to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            library.update_user(user_id, name or None)
            storage.save_users(library.list_users())

        elif choice == '8':
            user_id = input("Enter user ID of the user to delete: ")
            library.delete_user(user_id)
            storage.save_users(library.list_users())

        elif choice == '9':
            utils.print_users(library.list_users())

        elif choice == '10':
            name = input("Enter name to search: ")
            user_id = input("Enter user ID to search: ")
            results = library.search_users(name or None, user_id or None)
            utils.print_users(results)

        elif choice == '11':
            isbn = input("Enter ISBN of the book to check out: ")
            if library.check_out_book(isbn):
                print("Book checked out successfully.")
            else:
                print("Book not available.")
            storage.save_books(library.list_books())

        elif choice == '12':
            isbn = input("Enter ISBN of the book to check in: ")
            if library.check_in_book(isbn):
                print("Book checked in successfully.")
            else:
                print("Book not found.")
            storage.save_books(library.list_books())

        elif choice == '13':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
