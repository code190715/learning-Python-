//This is me learning python for the first time. 
/*Below are my notes.
Source of learning:
https://www.freecodecamp.org/news/the-python-handbook/amp/


Data Types in Python

• int 
• float
• complex for complex numbers
• bool for booleans
• list for lists
• tuple for tuples
• range for ranges
• dict for dictionaries
• set for sets




Operators in Python
Python operators are symbols that we use to run operations upon values and variables.
We can divide operators based on the kind of operation they perform:
	• assignment operator
	• arithmetic operators
	• comparison operators
	• logical operators
	• bitwise operators
plus some interesting ones like is and in.



The assignment operator is used to assign a value to a variable:
age = 8
Or to assign a variable value to another variable:
age = 8
anotherVariable = age




Python has a number of arithmetic operators:
-  +, 
- -, 
- *, 
- / (division), 
- %(remainder), 
- ** (exponentiation) , example: 4 ** 2  #16
- // (floor division) ,  example: 4 // 2  #2

+ is also used to concatenate String values:
"Roger" + " is a good dog"
#Roger is a good dog

We can combine the assignment operator with arithmetic operators:
	• +=
	• -=
	• *=
	• /=
	• %=
	• ..and so on


Boolean operators in Python
Python gives us the following boolean operators:
	• not
	• and
	• or
When working with True or False attributes, those work like logical AND, OR and NOT, and are often used in the if conditional expression evaluation:

condition1 = True
condition2 = False
not condition1 #False
condition1 and condition2 #False
condition1 or condition2 #True


Bitwise operators in Python
Some operators are used to work on bits and binary numbers:
	• & performs binary AND
	• | performs binary OR
	• ^ performs a binary XOR operation
	• ~ performs a binary NOT operation
	• << shift left operation
	• >> shift right operation
Bitwise operators are rarely used, only in very specific situations, but they are worth mentioning.



is and in in Python
is is called the identity operator. It is used to compare two objects and returns true if both are the same object. More on objects later.
in is called the membership operator. Is used to tell if a value is contained in a list, or another sequence. More on lists and other sequences later.


---

Strings in Python

You can convert a number to a string using the str class constructor:
str(8) #"8"



A string can be multi-line when defined with a special syntax, enclosing the string in a set of 3 quotes:
print("""Roger is
8
years old
""")
#double quotes, or single quotes
print('''
Roger is
8
years old
''')


In python, white space matters!! 


A string has a set of built-in methods, like:
	• isalpha() to check if a string contains only characters and is not empty
	• isalnum() to check if a string contains characters or digits and is not empty
	• isdecimal() to check if a string contains digits and is not empty
	• lower() to get a lowercase version of a string
	• islower() to check if a string is lowercase
	• upper() to get an uppercase version of a string
	• isupper() to check if a string is uppercase
	• title() to get a capitalized version of a string
	• startsswith() to check if the string starts with a specific substring
	• endswith() to check if the string ends with a specific substring
	• replace() to replace a part of a string
	• split() to split a string on a specific character separator
	• strip() to trim the whitespace from a string
	• join() to append new letters to a string
	• find() to find the position of a substring
and many more.


None of those methods alter the original string. They return a new, modified string instead. For example:
name = "Roger"
print(name.lower()) #"roger"
print(name) #"Roger"



In particular I think of len(), which gives you the length of a string:
name = "Roger"
print(len(name)) #5


The in operator lets you check if a string contains a substring:
name = "Roger"
print("ger" in name) #True


The way to go is to escape the double quote inside the string, with the \backslash character:
name = "Ro\"ger"


Given a string, you can get its characters using square brackets to get a specific item, given its index, starting from 0:
name = "Roger"
name[0] #'R'
name[1] #'o'
name[2] #'g'
Using a negative number will start counting from the end:
name = "Roger"
name[-1] #"r"
You can also use a range, using what we call slicing:
name = "Roger"
name[0:2] #"Ro"
name[:2] #"Ro"
name[2:] #"ger"




