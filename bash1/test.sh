#!/bin/bash

source function.sh

failed_test_count=0

function assert(){
	if [ $1 == $2 ]; then
		echo "OK"
	else
		failed_test_count=$(($failed_test_count + 1 ))
		echo "Error, received $1 but expected $2"
	fi
}


x=1 
y=10
addition $x $y
assert $result 11

x=10 
y=10
addition $x $y
assert $result 20

x=10 
y=10
subtraction $x $y
assert $result 0

x=10 
y=100
subtraction $x $y
assert $result -90

x=10 
y=10
multiplication $x $y
assert $result 100

x=-1 
y=10
multiplication $x $y
assert $result -10

x=10 
y=10
division $x $y
assert $result 1

x=100 
y=2
division $x $y
assert $result 50

x=10 
y=0
division $x $y 2> /dev/null
assert $? 1

x="hello"
y="world"
division $x $y 2> /dev/null
assert $? 1

exit $failed_test_count














