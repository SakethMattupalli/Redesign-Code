import json
import csv
from models import Book, User

class Storage:
    def __init__(self, book_file: str, user_file: str):
        self.book_file = book_file
        self.user_file = user_file

    def save_books(self, books: list):
        with open(self.book_file, 'w') as f:
            json.dump([book.__dict__ for book in books], f)

    def load_books(self) -> list:
        try:
            with open(self.book_file, 'r') as f:
                books_data = json.load(f)
                return [Book(**data) for data in books_data]
        except FileNotFoundError:
            return []

    def save_users(self, users: list):
        with open(self.user_file, 'w') as f:
            json.dump([user.__dict__ for user in users], f)

    def load_users(self) -> list:
        try:
            with open(self.user_file, 'r') as f:
                users_data = json.load(f)
                return [User(**data) for data in users_data]
        except FileNotFoundError:
            return []
