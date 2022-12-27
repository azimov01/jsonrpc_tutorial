from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            name="A good title",
            description="An excellent subtitle",
            author="Tom Christie",
            price="11",
        )

    def test_book_content(self):
        self.assertEqual(self.book.name, "A good title")
        self.assertEqual(self.book.description, "An excellent subtitle")
        self.assertEqual(self.book.author, "Tom Christie")
        self.assertEqual(self.book.price, "11")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "excellent subtitle")
        self.assertTemplateUsed(response, "books/book_list.html")
