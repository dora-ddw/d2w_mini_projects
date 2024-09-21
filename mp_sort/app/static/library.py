from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):
	array = list(range(num))
	random.seed(seed)
	random.shuffle(array)
 
	return array

def generate():
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the variable array
	array = gen_random_int(number, seed)
 
	# convert the items into one single string
	array_str = ''
 
	# the number should be separated by a comma
	for item in array[:-1]:
		array_str.append(str(item), ', ')
  
	# and a full stop should end the string.
	array_str.append('.')

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str
	return array_str


def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
	document.getElementById("generate").innerHTML = array_str
 
	# create a list of integers from the string of numbers
	numstring = gen_random_int
 
	# call your sort function, either bubble sort or insertion sort
		
	# create a string of the sorted numbers and store it in array_str
	
	array_str = None
	
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	pass

	array_str = None

	document.getElementById("sorted").innerHTML = array_str


