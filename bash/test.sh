#!/bin/bash

source function.sh

function assert(){
	x=$1
	y=$2
	if [ $x == $y ]; then
		echo -e "\e[1;32mOK\033[0m"
	else
		echo -e "\e[1;31mERROR\033[0m"
	fi
}

addition 0 0
assert $result 0

addition 0 1
assert $result 1

addition 10 10
assert $result 20

subtraction 3 1
assert $result 0

subtraction 30 1
assert $result 29

subtraction 0 1
assert $result -1

multiplication 2 2
assert $result 4

multiplication 100 100
assert $result 10000

multiplication 20 1
assert $result 20

division 10 0
assert $? 1

division 10 1
assert $result 10

division 4 2
assert $result 2


