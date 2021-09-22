#!/bin/bash

from function import *

total_errors = 0

def my_assert(x,y):
	global total_errors
	if x == y:
		print ("OK")
	else:
		print("Error, expected " + str(x) + ", received " + str(y))
		total_errors = total_errors + 1
		
		
		
x = 1
y = 3
result = addition(x, y)
my_assert(result,4)

x = 10
y = 30
result = addition(x, y)
my_assert(result,40)

x = 10
y = 30
result = division(x, y)
my_assert(result,0.3333333333333333)

try:
	x = 10
	y = 0
	result = division(x, y)
except ZeroDivisionError:
	print("OK")	

try:
	x = 10
	y = "hello"
	result = addition(x, y)
	my_assert(result,40)
except TypeError:
	print("OK")




exit(total_errors)