from function import *

############################################

def test(x,y,text):
	if x==y:
		print('\033[32m' + "OK - " + text + '\033[0m')
	else:
		print('\033[31m' + "ERROR - " + text + '\033[0m')

############################################

x=0
y=0
expected_result=0
result=addition(x,y)
test(result,expected_result,str(x) + "+" + str(y) + "=" + str(expected_result) + ", result was " + str(result))

x=1
y=2
expected_result=3
result=addition(x,y)
test(result,expected_result,str(x) + "+" + str(y) + "=" + str(expected_result) + ", result was " + str(result))

x=-1
y=-2
expected_result=-3
result=addition(x,y)
test(result,expected_result,str(x) + "+" + str(y) + "=" + str(expected_result) + ", result was " + str(result))

x=10
y=5
expected_result=5
result=subtraction(x,y)
test(result,expected_result,str(x) + "-" + str(y) + "=" + str(expected_result) + ", result was " + str(result))

x=-1
y=-2
expected_result=1
result=subtraction(x,y)
test(result,expected_result,str(x) + "-" + str(y) + "=" + str(expected_result) + ", result was " + str(result))

x=0
y=0
expected_result=0
result=subtraction(x,y)
test(result,expected_result,str(x) + "-" + str(y) + "=" + str(expected_result) + ", result was " + str(result))

x=0
y=0
expected_result=0
result=multiplication(x,y)
test(result,expected_result,str(x) + "*" + str(y) + "=" + str(expected_result) + ", result was " + str(result))

x=100
y=100
expected_result=10000
result=multiplication(x,y)
test(result,expected_result,str(x) + "*" + str(y) + "=" + str(expected_result) + ", result was " + str(result))

x=-1
y=-1
expected_result=1
result=multiplication(x,y)
test(result,expected_result,str(x) + "*" + str(y) + "=" + str(expected_result) + ", result was " + str(result))

x=10
y=5
expected_result=2
result=division(x,y)
test(result,expected_result,str(x) + "/" + str(y) + "=" + str(expected_result) + ", result was " + str(result))

x=10
y=5
expected_result=2.0
result=division(x,y)
test(result,expected_result,str(x) + "/" + str(y) + "=" + str(expected_result) + ", result was " + str(result))

x=1
y=5
expected_result=0.2
result=division(x,y)
test(result,expected_result,str(x) + "/" + str(y) + "=" + str(expected_result) + ", result was " + str(result))

x=10
y=0
expected_result=-1
try:
	result=division(x,y)
except ZeroDivisionError:
	result=-1
test(result,expected_result,"Division by 0 should fail with ZeroDivisionError")