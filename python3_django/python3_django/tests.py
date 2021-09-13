from django.test import TestCase
from django.urls import reverse
from django.test.utils import override_settings
import json
from rest_framework import status

from . import views
        
class CreateHostnameTest(TestCase):
        
    def test_multiply1(self):
        response = self.client.post(
            reverse('api_view'),
            {'data':'3*3'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'9')
        
    def test_multiply2(self):
        response = self.client.post(
            reverse('api_view'),
            {'data':'3000*3000'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'9000000')
        
    def test_division1(self):
        response = self.client.post(
            reverse('api_view'),
            {'data':'3/3'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'1.0')
        
    def test_division2(self):
        response = self.client.post(
            reverse('api_view'),
            {'data':'99/88'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'1.125')
        
    def test_division_by_zero(self):
        response = self.client.post(
            reverse('api_view'),
            {'data':'3/0'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'"division by 0"')
        
    def test_empty(self):
        response = self.client.post(
            reverse('api_view'),
            data="",
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'"invalid input"')
        
    def test_addition1(self):
        response = self.client.post(
            reverse('api_view'),
            {'data':'1+1'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'2')
        
    def test_addition1(self):
        response = self.client.post(
            reverse('api_view'),
            {'data':'100+1'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'101')
        
    def test_substraction1(self):
        response = self.client.post(
            reverse('api_view'),
            {'data':'1-1'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'0')
        
    def test_substraction2(self):
        response = self.client.post(
            reverse('api_view'),
            {'data':'1-100'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'-99')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        