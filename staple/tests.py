import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from staple.models import Document
from staple.views import DocumentForm
from django.urls import reverse_lazy

# Create your tests here.

class StapleTestCase(TestCase):
    def test_true_is_true(self):
        '''Tests if True ==  True'''
        self.assertEqual(True, True)

    def test_document_slug_on_save(self):
        '''Test the slug generated when saving a Document'''
        user = User()
        user.save()

        doc = Document(title='The 5Gs', content='Good God Girl Get a Grip', author=user)
        doc.save()

        self.assertEqual(doc.slug, 'the-5gs')

class DocumentListViewTest(TestCase):
    def test_document_list_page(self):
        '''Tests if List View works'''
        user = User.objects.create()

        Document.objects.create(title='This Boy is A Bottom', content='This boy is a bottom', author=user)
        Document.objects.create(title='This is my hair', content='I don\'t wear wigs', author=user)

        # Issue a GET response to the Doc List page.
        # When we make a request, we get a response back.
        response = self.client.get('/documents/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the number of pages passed to the template
        # matches the number of pages we have in the database
        responses = response.context['documents']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Document: This Boy is A Bottom>', '<Document: This is my hair>'],
            ordered=False
        )

class DocumentDetailViewTests(TestCase):
    """ Tests the doc details page loads for a specific page """

    def test_detail_page(self):
        user = User.objects.create()

        doc = Document.objects.create(title="My Detail Page", content="details details schmeetales", author=user)

        slug = doc.slug
        response = self.client.get(f'/documents/{slug}/')

        self.assertEqual(response.status_code, 200)