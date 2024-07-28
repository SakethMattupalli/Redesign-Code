# Library Management System

This is a simple Library Management System implemented in Python. It allows you to manage books and users, check out and check-in books, and track book availability through a command-line interface (CLI). The system uses file-based storage (JSON) for persistent data storage.

## Features

- **Manage Books:**
  - Add new books
  - Update existing books
  - Delete books
  - List all books
  - Search books by title, author, or ISBN

- **Manage Users:**
  - Add new users
  - Update existing users
  - Delete users
  - List all users
  - Search users by name or user ID

- **Book Transactions:**
  - Check out books
  - Check in books

- **Persistent Storage:**
  - Uses JSON files to store book and user data

## Project Structure

<pre>
Redesign-Code/
├── main.py
├── models.py
├── storage.py
├── utils.py
└── README.md
</pre>

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/SakethMattupalli/Redesign-Code.git
    ```

2. **Ensure you have Python installed:**
    - You can download Python from [python.org](https://www.python.org/).

3. **Run the application:**

    ```sh
    python main.py
    ```

## Usage

When you run the application, you will see a menu with options to manage books and users, perform check out and check in operations, and search for books and users. Enter the corresponding number for the action you want to perform.



# User Menu
<pre>
------------------------------
Library Management System
1. Add Book
2. Update Book
3. Delete Book
4. List Books
5. Search Books
6. Add User
7. Update User
8. Delete User
9. List Users
10. Search Users
11. Check Out Book
12. Check In Book
13. Exit
------------------------------
</pre>

### Some Examples

1. **Add a new book:**

    ```
    Enter your choice: 1
    Enter book title: Theory of Relativity
    Enter book author: A.E
    Enter book ISBN: 1234
    Enter number of copies: 5
    ```

2. **List all books:**

    ```
    Enter your choice: 4
    ```

    Output:
    ```
    Title: Theory of Relativity, Author: A.E, ISBN: 1234, Copies: 5
    ```

3. **Add a new user:**

    ```
    Enter your choice: 6
    Enter user name: MSD
    Enter user ID: 7
    ```

4. **Check out a book:**

    ```
    Enter your choice: 1
    Enter ISBN of the book to check out: 1234
    Book checked out successfully.
    ```


