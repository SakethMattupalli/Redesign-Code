def print_menu():
    print()
    print('---'*10)
    print("Library Management System")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. List Books")
    print("5. Search Books")
    print("6. Add User")
    print("7. Update User")
    print("8. Delete User")
    print("9. List Users")
    print("10. Search Users")
    print("11. Check Out Book")
    print("12. Check In Book")
    print("13. Exit")
    print('---'*10)

def print_books(books):
    if not books:
        print("No books found.")
    for book in books:
        print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Copies: {book.copies}")

def print_users(users):
    if not users:
        print("No users found.")
    for user in users:
        print(f"Name: {user.name}, User ID: {user.user_id}")
