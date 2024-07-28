import json
import csv
from typing import List, Optional

class Book:
    def __init__(self, title: str, author: str, isbn: str, copies: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

class User:
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id

class Library:
    def __init__(self):
        self.books: List[Book] = []
        self.users: List[User] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def update_book(self, isbn: str, title: Optional[str] = None, author: Optional[str] = None, copies: Optional[int] = None):
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if author:
                    book.author = author
                if copies is not None:
                    book.copies = copies
                return book
        return None

    def delete_book(self, isbn: str):
        self.books = [book for book in self.books if book.isbn != isbn]

    def list_books(self) -> List[Book]:
        return self.books

    def search_books(self, title: Optional[str] = None, author: Optional[str] = None, isbn: Optional[str] = None) -> List[Book]:
        results = self.books
        if title:
            results = [book for book in results if book.title == title]
        if author:
            results = [book for book in results if book.author == author]
        if isbn:
            results = [book for book in results if book.isbn == isbn]
        return results

    def add_user(self, user: User):
        self.users.append(user)

    def update_user(self, user_id: str, name: Optional[str] = None):
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                return user
        return None

    def delete_user(self, user_id: str):
        self.users = [user for user in self.users if user.user_id != user_id]

    def list_users(self) -> List[User]:
        return self.users

    def search_users(self, name: Optional[str] = None, user_id: Optional[str] = None) -> List[User]:
        results = self.users
        if name:
            results = [user for user in results if user.name == name]
        if user_id:
            results = [user for user in results if user.user_id == user_id]
        return results

    def check_out_book(self, isbn: str) -> Optional[Book]:
        for book in self.books:
            if book.isbn == isbn and book.copies > 0:
                book.copies -= 1
                return book
        return None

    def check_in_book(self, isbn: str) -> Optional[Book]:
        for book in self.books:
            if book.isbn == isbn:
                book.copies += 1
                return book
        return None
