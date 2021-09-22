#!/bin/python3

from function import *
import unittest

class TestCalculator(unittest.TestCase):

	def test_addition(self):
		x=1
		y=2
		result=addition(x,y)
		self.assertEqual(result, 3)

	def test_division(self):
		x=1
		y=0
		with self.assertRaises(ZeroDivisionError):
			division(x,y)

		x="hello"
		y="world"
		with self.assertRaises(TypeError):
			division(x,y)


if __name__ == '__main__':
	unittest.main()