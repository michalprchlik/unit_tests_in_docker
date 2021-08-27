#!/bin/bash

source function.sh

###############################################################

###############################################################

x=0
y=1
addition ${x} ${y}
echo "${x}+${y}=${result}"

x=3
y=1
subtraction ${x} ${y}
echo "${x}-${y}=${result}"

x=4
y=5
multiplication ${x} ${y}
echo "${x}*${y}=${result}"

x=10
y=2
division ${x} ${y}
echo "${x}/${y}=${result}"