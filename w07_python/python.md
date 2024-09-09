# PYTHON



## Variables and Data types
##### Variables
- a smart way to store values in containers
- you dont require to specify the type while storing them
- you can store the return value of the input function in a variable and use that variable in the print function
##### Data Types
- int or integers: e.g 25 (any whole number, negative or positive)
- str or strings: e.g 'hello' or '25' (any character surrounded with quotes)
- float: e.g 1.2 or 1.0 (any number with a decimal point)
- booleans: e.g True or False 
- NoneType: e.g None (absence of a value)

##### Formatted strings
- use 'f' before the quotes in a string so the python interpreter interpretes that string literally, you can then plug in the variables inside curly braces

## Conditionals
- the return value for the input function is a string, hence the strings in the input function
- if you prompt the user to input a number then you must type cast that return value to int or float to be able to use it
- if you dont do this, you get an error or an exception, hence the program crashes.
- to use conditionals, you use if, elif, else to do something is certain conditions are true
- these are keywords or statements
- python uses indentation to scope code
- pep8 standard recommends a tab or 4 spaces for indentation
- if you fail to type cast the return value of the input function to int when dealing with numbers, you get a TypeError, meaning python didnt recieve the specified type of int, it got a string instead. This is called an exception.
- when you have an exception, the first thing to look at is the type of exception: ValueError, TypeError, etc
- you cannot compare a string with an integer, says the error.
- next, check the Traceback for particular code and the particular line on which the error occured

 ## Data Structures
 ### Sequences
 - sequences are indexed data structures, like strings, lists, etc
- python is zero indexed, meaning it starts counting numbers from 0
 - you can index into a sequence
 - to print out the entire content, use a loop

 ##### Strings
 strings are a type of data structure, storing a single value. they are mutable.

 ##### Lists
 Lists are a type of data structure used to store a list of items. they are mutable.
 - a number of methods are possible with a list, including appending, sorting, etc.

 ##### Tuples
 Tuples a immutable, unchangeable data structures, used to to store multiple values. it is used when a single variable consists of two parts. like a coordinate x and y

##### Sets
- collection of unique values. unindexed. each value exists only once. used when you dont care about the order of the list. you can remove, add elements from a set, they are mutable

### Dictionaries
- maps items to a value, in a pair. They exist in key-value pairs
- you can look up the value in dictionaries through their keys
- they are not indexed
- you can add to a dictionary


### Loops
- loops are used to do something over and over
- it means go through every element in the list and for each element, set i as a variable to that element, and print that 
- loops can be used on any sequence
- it is easier to use the range function for looping numbers
- the range function excludes the last number because python is 0 indexed.

### functions
- create a function to perform an operation which you can refference any time, from any where.
- others can use your functions as well, by importing them as modules

### OOP
- Object Oriented Programming using classes
- classes are a template for a type of objects
- methods are functions inside classes
- magic methods take a self parameter

### Functional Programming
##### Decorators
- Python uses decorators to modify the behaviour of functions
- decorators are functions that take a function as input and returns a modified version of that funtion as output

##### Lambda Functions
- These are anonymous functions without a name
- if you try to sort the content of a dictionary you get an exception because dictionaries are not indexed, but the you can only access values from their keys
- so to sort a dictionary by its keys, you have to run a function that return the keys of that dictionary or for values, that return its values, then sort.
- however, defining a function just to use it once, is not necessary, yu simply define it as anonymous

## Exceptions
- exceptions mean that something in the code didnt go as expected
- you use try, except, else blocks to catch exceptions in programming