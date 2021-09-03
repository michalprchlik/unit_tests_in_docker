from function import *
import unittest

############################################

class TestCalculator(unittest.TestCase):

	def test_addition(self):
		x=0
		y=0
		expected_result=0
		result=addition(x,y)
		text=str(x) + "+" + str(y) + "=" + str(expected_result)
		self.assertEqual(expected_result, result, text)
		
		x=1
		y=2
		expected_result=3
		result=addition(x,y)
		text=str(x) + "+" + str(y) + "=" + str(expected_result)
		self.assertEqual(expected_result, result, text)
		
		x=-1
		y=-2
		expected_result=-3
		result=addition(x,y)
		text=str(x) + "+" + str(y) + "=" + str(expected_result)
		self.assertEqual(expected_result, result, text)
		
	def test_addition_exception(self):
		x="hello"
		y="world"
		with self.assertRaises(TypeError):
			addition(x,y)	
		
	def test_subtraction(self):
		x=10
		y=5
		expected_result=5
		result=subtraction(x,y)
		text=str(x) + "-" + str(y) + "=" + str(expected_result)
		self.assertEqual(expected_result, result, text)
		
		x=-1
		y=-2
		expected_result=1
		result=subtraction(x,y)
		text=str(x) + "-" + str(y) + "=" + str(expected_result)
		self.assertEqual(expected_result, result, text)
		
		x=0
		y=0
		expected_result=0
		result=subtraction(x,y)
		text=str(x) + "-" + str(y) + "=" + str(expected_result)
		self.assertEqual(expected_result, result, text)
		
	def test_addition_exception(self):
		x="hello"
		y="world"
		with self.assertRaises(TypeError):
			subtraction(x,y)
		
	def test_multiplication(self):
		x=-1
		y=-2
		expected_result=2
		result=multiplication(x,y)
		text=str(x) + "*" + str(y) + "=" + str(expected_result)
		self.assertEqual(expected_result, result, text)
		
		x=100
		y=100
		expected_result=10000
		result=multiplication(x,y)
		text=str(x) + "*" + str(y) + "=" + str(expected_result)
		self.assertEqual(expected_result, result, text)
		
		x=1
		y=2
		expected_result=2
		result=multiplication(x,y)
		text=str(x) + "*" + str(y) + "=" + str(expected_result)
		self.assertEqual(expected_result, result, text)
		
		x=1000000000000000
		y=1000000000000000
		expected_result=1000000000000000000000000000000
		result=multiplication(x,y)
		text=str(x) + "*" + str(y) + "=" + str(expected_result)
		self.assertEqual(expected_result, result, text)
		
	def test_multiplication_exception(self):
		x="hello"
		y="world"
		with self.assertRaises(TypeError):
			multiplication(x,y)	
		
	def test_division(self):
		x=10
		y=5
		expected_result=2
		result=division(x,y)
		text=str(x) + "/" + str(y) + "=" + str(expected_result)
		self.assertEqual(expected_result, result, text)
		
		x=10
		y=5
		expected_result=2.0
		result=division(x,y)
		text=str(x) + "/" + str(y) + "=" + str(expected_result)
		self.assertEqual(expected_result, result, text)
		
		x=1
		y=5
		expected_result=0.2
		result=division(x,y)
		text=str(x) + "/" + str(y) + "=" + str(expected_result)
		self.assertEqual(expected_result, result, text)

	def test_division_exception(self):
		x=10
		y=0
		with self.assertRaises(ZeroDivisionError):
			division(x,y)
		
		x="hello"
		y="world"
		with self.assertRaises(TypeError):
			division(x,y)			

############################################

if __name__ == '__main__':
	unittest.main()
