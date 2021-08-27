#!/bin/bash

function addition(){
	x=$1
	y=$2
	result=$(echo $(($x+$y)))
}

function subtraction(){
	x=$1
	y=$2
	result=$(echo $(($x-$y)))
}

function multiplication(){
	x=$1
	y=$2
	result=$(echo $(($x*$y)))
}

function division(){
	x=$1
	y=$2
	result=$(echo $(($x/$y)))
}