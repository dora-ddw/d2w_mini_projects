# from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):
	array = list(range(number))
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
	# the number should be separated by a comma
	# and a full stop should end the string.
	array_str = str(array)
	array_str.remove('[', ']')
	array_str.append('.')
 
	# another method
	array_str = ''
	for item in array[:-1]:
		array_str.append(str(item), ', ')
	array_str.append(str(array[-1]), '.')

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str
	# document.getElementbyId("generate").innerHTML
	return array_str

def insertionSort(numlist):
    while not is_sorted:        
        end = len(numlist)
        is_sorted = False # check if the string is sorted
        for ptr in range(1, end):
            rightptr = ptr
            leftptr = rightptr - 1 # left side of the item of interest will be sorted
            while leftptr >= 0 and numlist[rightptr] < numlist[leftptr]:
                numlist[rightptr], numlist[leftptr] = numlist[leftptr], numlist[rightptr]
                leftptr -= 1
                rightptr -= 1
                is_sorted = True # by the time the pointer reaches the end, all elements should have been sorted
    return numlist

def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.
	'''
	# get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
	document.getElementById("generate").innerHTML = array_str
 
	# create a list of integers from the string of numbers
	numslist = gen_random_int()
 
	# call your sort function, either bubble sort or insertion sort
	sortedlist = insertionSort(numslist)	
 
	# create a string of the sorted numbers and store it in array_str
 	# array_str = str(elements for elements in array) # idk if it works liddis
	# array_str = ''
	# for elements in array:
	# 	array_str.append(str(elements))
	array_str = str(numslist)
	array_str.remove('[', ']')
	array_str.append('.')
	
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

	# Get the numbers from a string variable "value"
	# Split the string using comma as the separator and convert them to a list of numbers
	valuenums = []
	for item in value:
		if item.isnumeric():
			valuenums.append(int(item))

	# call your sort function, either bubble sort or insertion sort
	sortedvalues = insertionSort(valuenums)

	# create a string of the sorted numbers and store the final string to the variable array_str
	array_str = []
	for nummer in sortedvalues:
		array_str.append(str(nummer))

	document.getElementById("sorted").innerHTML = array_str


