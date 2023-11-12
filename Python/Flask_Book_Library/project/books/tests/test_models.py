import unittest

from project.books.models import Book


class BookModelTest(unittest.TestCase):
    def test_book_valid(self):
        book = Book(name="Name Surname", author="Author", year_published=2023, book_type="Type")
        self.assertEqual(book.name, "Name Surname")

    def test_name_invalid(self):
        with self.assertRaises(ValueError):
            Book(name="<script>alert('XSS');</script>", author="Author", year_published=2023, book_type="Type")

    def test_author_invalid(self):
        with self.assertRaises(ValueError):
            Book(name="Name Surname", author="<script>alert('XSS');</script>", year_published=2023, book_type="Type")
