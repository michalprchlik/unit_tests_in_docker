from django.test import TestCase
from django.urls import reverse

class test_hello_world(TestCase):
	def test_get(self):
		response = self.client.get(reverse('api_view'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, b'"Hello world"')
		
class CalculatorTest(TestCase):
	def test_addition(self):
		response = self.client.post(reverse('api_view'), {"data": "3*3"}, content_type="application/json")
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.content, b'9')