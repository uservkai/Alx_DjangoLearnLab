from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

#testing creating, updating, deleting,  books
class BookAPITestCase(APITestCase):
    def setUp(self):
        #create test users
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.other_user = User.objects.create_user(username='otheruser', password='otherpass')
        
        #Create test author and book
        self.author = Author.objects.create(name='Author One')
        self.book = Book.objects.create(title='Book One', publication_year=2020, author=self.author)
        
        #auth token setup (since using TokenAuthentication)
        self.client.login(username='testuser', password='testpass')
        
    def test_create_book_authenticated(self):
        url = reverse('book-create')
        data = {
            'title': 'Book Two',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Book Two')
        self.assertEqual(Book.objects.count(), 2)
        
    def test_create_book_unauthenticated(self):
        self.client.logout()
        url = reverse('book-create')
        data = {
            'title': 'Book Three',
            'publication_year': 2019,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_update_book_authenticated(self):
        url = reverse('book-update', args=[self.book.id])
        data = {
            'title': 'Book One - Revised',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Book One - Revised')
        
    def test_update_book_unauthenticated(self):
        self.client.logout()
        url = reverse('book-update', args=[self.book.id])
        data = {
            'title': 'Book One - Hacked',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_delete_book_authenticated(self):
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
        
    def test_delete_book_unauthenticated(self):
        self.client.logout()
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_filter_books_by_author(self):
        url = reverse('book-list') + '?author={}'.format(self.author.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=One'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('One' in book['title'] for book in response.data))
        
    def test_order_books_by_publication_year(self):
        #create another book for ordering test
        Book.objects.create(title='Book Zero', publication_year=2018, author=self.author)
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))