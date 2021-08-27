#!/bin/bash

source function.sh

###############################################################

function assert(){
	if [ $1 == $2 ]; then
		echo -e "\e[1;32mOK - ${3}\033[0m"
	else
		echo -e "\e[1;31mERROR - ${3}\033[0m"
	fi
}

###############################################################

x=0
y=0
expected_result=0
addition ${x} ${y}
assert ${result} $expected_result "${x}+${y}=${expected_result}, result was ${result}"

x=1
y=1
expected_result=2
addition ${x} ${y}
assert ${result} $expected_result "${x}+${y}=${expected_result}, result was ${result}"

x=10
y=10
expected_result=20
addition ${x} ${y}
assert ${result} $expected_result "${x}+${y}=${expected_result}, result was ${result}"

x=3
y=1
expected_result=2
subtraction ${x} ${y}
assert ${result} $expected_result "${x}-${y}=${expected_result}, result was ${result}"

x=30
y=1
expected_result=29
subtraction ${x} ${y}
assert ${result} $expected_result "${x}-${y}=${expected_result}, result was ${result}"

x=0
y=1
expected_result=-1
subtraction ${x} ${y}
assert ${result} $expected_result "${x}-${y}=${expected_result}, result was ${result}"

x=2
y=2
expected_result=4
multiplication ${x} ${y}
assert ${result} $expected_result "${x}*${y}=${expected_result}, result was ${result}"

x=100
y=100
expected_result=10000
multiplication ${x} ${y}
assert ${result} $expected_result "${x}*${y}=${expected_result}, result was ${result}"

x=20
y=2
expected_result=40
multiplication ${x} ${y}
assert ${result} $expected_result "${x}*${y}=${expected_result}, result was ${result}"

x=10
y=0
expected_result=1
division ${x} ${y}
assert $? $expected_result "Division by 0 should fail with exit code 1. Exit code was $?"

x=10
y=1
expected_result=10
division ${x} ${y}
assert ${result} $expected_result "${x}/${y}=${expected_result}, result was ${result}"

x=4
y=2
expected_result=2
division ${x} ${y}
assert ${result} $expected_result "${x}/${y}=${expected_result}, result was ${result}"
