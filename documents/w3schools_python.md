# W3Schools Python Tutorial

Source: https://www.w3schools.com/python/

# Python Tutorial

## Learn Python

Python is a popular programming language.

Python can be used on a server to create web applications.

Tip: Sign in to track your progress.

## Learning by Examples

With our "Try it Yourself" editor, you can edit Python code and view the result.

```python
print("Hello, World!")
```

## Example

Click on the "Try it Yourself" button to see how it works.

## Python File Handling

In our File Handling section you will learn how to open, read, write, and 
delete files.

Python File Handling

## Python Database Handling

In our database section you will learn how to access and work with MySQL and MongoDB databases:

Python MySQL Tutorial

Python MongoDB Tutorial

## Python Exercises

Many chapters in this tutorial end with an exercise where you can check your level of knowledge.



## Python Examples

Learn by examples! This tutorial supplements all explanations with clarifying examples.



## Python Quiz

Test your Python skills with a quiz.



## Track Your Progress

- View your completed tutorials, exercises, and quizzes
- Keep an eye on your progress and daily streaks
- Join the leaderboard and compete with others
- Get your own avatar and unlock new skins
- Create your own personal website



Note: This is an optional feature. You can study at W3Schools without creating an account.

## Python Reference

You will also find complete function and method references:

## Download Python

Download Python from the official Python web site:
  https://python.org

## Kickstart your career

Get certified by completing the  course


---

# Python Introduction

## What is Python?

Python is a popular programming language. It was created by Guido van Rossum, 
and released in 1991.

It is used for:

- web development (server-side),
- software development,
- mathematics,
- system scripting.

## What can Python do?

- Python can be used on a server to create web applications.
- Python can be used alongside software to create workflows.
- Python can connect to database systems. It can also read and modify files.
- Python can be used to handle big data and perform complex mathematics.
- Python can be used for rapid prototyping, or for production-ready software development.

## Why Python?

- Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
- Python has a simple syntax similar to the English language.
- Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
- Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
- Python can be treated in a procedural way, an object-oriented way or a functional way.

## Good to know

- The most recent major version of Python is Python 3, which we shall be using in this tutorial.
- In this tutorial Python will be written in a text editor. It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files.

## Python Syntax compared to other programming languages

- Python was designed for readability, and has some similarities to the English language with influence from mathematics.
- Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
- Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

```python
print("Hello, World!")
```

## Example

## Video: Python Introduction


---

# Python Getting Started

## Get Started With Python

At W3Schools, you can try Python without installing anything.

Our Online Python Editor runs directly in your browser, and shows both the code and the result:

```python
print("Hello, World!")
```

## Example

This editor will be used in the entire tutorial to demonstrate the different aspects of Python.

## Python Install

However, if you want to run Python on your own computer, follow the instructions below.

Many Windows PCs and Mac computers already have Python pre-installed.

To check if Python is installed on Windows, search in the start bar for Python or run the following on the Command Line (cmd.exe):

```python
C:\Users\Your Name>python --version
```

To check if you have python installed on a Linux or Mac, then on linux open the command line or on Mac open the Terminal and type:

```python
python --version
```

If Python is not installed on your computer, you can download it for free from the official website: https://www.python.org/

## Python Quickstart

Python is an interpreted programming language, this means that as a developer you write Python (.py) files in a text editor and then put those files into the python interpreter to be executed.

Let's write our first Python file, called hello.py, which can be done in any text editor:

hello.py:

Simple as that. Save your file. Open your command line, navigate to the directory where you saved your file, and run:

```python
C:\Users\Your Name>python hello.py
```

The output should be:

```python
Hello, World!
```

Congratulations, you have written and executed your first Python program.

## Python Version

To check the Python version of the editor, you can find it by importing the sys module:

```python
import sys

print(sys.version)
```

## Example

Check the Python version of the editor:

You will learn more about importing modules in our 
Python Modules chapter.

## The Python Command Line

To test a short amount of code in python sometimes it is quickest and easiest not to write the code in a file. This is made possible because Python can be run as a command line itself.

Type the following on the Windows, Mac or Linux command line:

```python
C:\Users\Your Name>python
```

```python
C:\Users\Your Name>py
```

From there you can write any python code, including our hello world example from earlier in the tutorial:

```python
C:\Users\Your Name>python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello, World!")
```

Which will write "Hello, World!" in the command line:

```python
C:\Users\Your Name>python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello, World!")
Hello, World!
```

Whenever you are done in the python command line, you can simply type the following to quit the python command line interface:

```python
exit()
```

## Video: Python Get Started


---

# Python Syntax

## Execute Python Syntax

As we learned in the previous page, Python syntax can be executed by writing directly in the Command Line:

```python
>>> print("Hello, World!")
    Hello, World!
```

Or by creating a python file on the server, using the .py file extension, and running it in the Command Line:

```python
C:\Users\Your Name>python myfile.py
```

## Python Indentation

Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability 
only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.

```python
if 5 > 2: 
print("Five is greater than two!")
```

## Example

Python will give you an error if you skip the indentation:

```python
if 5 > 2:
print("Five is greater than two!")
```

## Example

Syntax Error:

The number of spaces is up to you as a programmer, the most common use is four, but it has 
to be at least one.

```python
if 5 > 2: print("Five is greater than two!") 
if 5 > 2:        print("Five is greater than two!")
```

## Example

You have to use the same number of spaces in the same block of code, 
otherwise Python will give you an error:

```python
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than 
  two!")
```

## Example

Syntax Error:

## Python Variables

In Python, variables are created when you assign a value to it:

Example
Variables in Python:

  x = 5y = "Hello, World!"



Python has no command for declaring a variable.
You will learn more about variables in the 
Python Variables chapter.

Comments
Python has commenting capability for the purpose of in-code documentation.
Comments start with a #, and Python will render the rest of the line as a comment:

Example
Comments in Python:

#This is a comment.
print("Hello, World!")








Video: Python Syntax































★
+1

```python
x = 5y = "Hello, World!"
```

## Example

Variables in Python:

Python has no command for declaring a variable.

You will learn more about variables in the 
Python Variables chapter.

## Comments

Python has commenting capability for the purpose of in-code documentation.

Comments start with a #, and Python will render the rest of the line as a comment:

Example
Comments in Python:

#This is a comment.
print("Hello, World!")








Video: Python Syntax































★
+1

```python
#This is a comment.
print("Hello, World!")
```

## Example

Comments in Python:

## Video: Python Syntax


---

# Python Statements

## Statements

A computer program is a list of "instructions" to be "executed" by a computer.

In a programming language, these programming instructions are called statements.

The following statement prints the text "Python is fun!" to the screen:

```python
print("Python is fun!")
```

## Example

In Python, a statement usually ends when the line ends. You do not need to use a semicolon (;) like in many other programming languages (for example, Java or C).

## Many Statements

Most Python programs contain many statements.

The statements are executed one by one, in the same order as they are written:

```python
print("Hello World!")print("Have a good day.")print("Learning Python is fun!")
```

## Example

From the example above, we have three statements:

- print("Hello World!")
- print("Have a good day.")
- print("Learning Python is fun!")

The first statement is executed first (print "Hello World!").
Then the second statement is executed (print "Have a good day.").
And at last, the third statement is executed (print "Learning Python is fun!").

## Semicolons (Optional, Rarely Used)

Semicolons are optional in Python. You can write multiple statements on one line by separating them with ; but this is 
rarely used because it makes it hard to read:

```python
print("Hello"); print("How are 
    you?"); print("Bye bye!")
```

## Example

However, if you put two statements on the same line without a separator (newline or ;), Python will give an error:

```python
print("Python is fun!") print("Really!")
```

## Example

Result:

Best practice: Put each statement on its own line so your code is easy to understand.


---

# Python Output / Print

## Print Text

You have already learned that you can use the print() function to display text or output values:

```python
print("Hello World!")
```

## Example



You can use the print() function as many times as you want. Each call prints text on a new line by default:

```python
print("Hello World!")
    print("I am learning Python.")
    print("It is awesome!")
```

## Example



## Double Quotes

Text in Python must be inside quotes. You can use either " double quotes or ' single quotes:

```python
print("This will work!")
    print('This will also work!')
```

## Example



If you forget to put the text inside quotes, Python will give an error:

```python
print(This will cause an error)
```

## Example

Result:



## Print Without a New Line

By default, the print() function ends with a new line.

If you want to print multiple words on the same line, you can use the end parameter:

```python
print("Hello World!", end=" ")
    print("I will print on the same line.")
```

## Example



Note that we add a space after end=" " for better readability.


---

# Python Output Numbers

## Print Numbers

You can also use the print() function to display numbers:

However, unlike text, we don't put numbers inside double quotes:

```python
print(3)
    print(358)
    print(50000)
```

## Example



You can also do math inside the print() function:

```python
print(3 + 3)
    print(2 * 5)
```

## Example



## Mix Text and Numbers

You can combine text and numbers in one output by separating them with a comma:

```python
print("I am", 35, "years old.")
```

## Example



You will learn more about combining text and variables in the Python Variables and Python Strings chapters.


---

# Python Comments

Comments can be used to explain Python code.

Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.

## Creating a Comment

Comments starts with a #, and Python will 
ignore them:

```python
#This is a comment
print("Hello, World!")
```

## Example

Comments can be placed at the end of a line, and Python will ignore the rest 
of the line:

```python
print("Hello, World!") #This is a comment
```

## Example

A comment does not have to be text that explains the code, it can also be used to 
prevent Python from executing code:

```python
#print("Hello, World!")print("Cheers, Mate!")
```

## Example

## Multiline Comments

Python does not really have a syntax for multiline comments.

To add a multiline comment you could insert a # for each line:

```python
#This is a comment#written in#more than just one lineprint("Hello, 
  World!")
```

## Example

Or, not quite as intended, you can use a multiline string.

Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:

```python
"""This is a commentwritten in more than just 
  one line"""print("Hello, World!")
```

## Example

As long as the string is not assigned to a variable, Python will read the code, but then ignore it, and you have made a multiline comment.

## Video: Python Comments


---

# Python Variables

## Variables

Variables are containers for storing data values.

## Creating Variables

Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

```python
x = 5
y = "John"
print(x)
print(y)
```

## Example

Variables do not need to be declared with any particular type, and can even change type after they have been set.

```python
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
```

## Example

## Casting

If you want to specify the data type of a variable, this can be done with casting.

```python
x = 
  str(3)    # x will be '3'y = int(3)    # y 
  will be 3z = float(3)  # z will be 3.0
```

## Example

## Get the Type

You can get the data type of a variable with the type() function.

```python
x = 5y = "John"print(type(x))print(type(y))
```

## Example

## Single or Double Quotes?

String variables can be declared either by using single or double quotes:

```python
x = "John"# is the same asx = 
  'John'
```

## Example

## Case-Sensitive

Variable names are case-sensitive.

```python
a = 4A = 
  "Sally"#A will not overwrite a
```

## Example

This will create two variables:

## Video: Python Variables


---

# Python - Variable Names

## Variable Names

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords.

```python
myvar = "John"my_var = "John"_my_var = "John"myVar = "John"
  MYVAR = "John"myvar2 = "John"
```

## Example

Legal variable names:

```python
2myvar = "John"my-var = "John"
  my var = "John"
```

## Example

Illegal variable names:

Remember that variable names are case-sensitive

## Multi Words Variable Names

Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

## Camel Case

Each word, except the first, starts with a capital letter:

## Pascal Case

Each word starts with a capital letter:

## Snake Case

Each word is separated by an underscore character:

## Video: Python Variable Names


---

# Python Variables - Assign Multiple Values

## Many Values to Multiple Variables

Python allows you to assign values to multiple variables in one line:

```python
x, y, z = "Orange", "Banana", "Cherry"print(x)print(y)print(z)
```

## Example

Note: Make sure the number of variables matches the number of values, or else you will get an error.

## One Value to Multiple Variables

And you can assign the same value to multiple variables in one line:

```python
x = y = z = "Orange"print(x)print(y)print(z)
```

## Example

## Unpack a Collection

If you have a collection of values in a list,
  tuple etc.
Python allows you to extract the values into variables. This is called unpacking.



```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
```

## Example

Unpack a list:

Learn more about unpacking in our Unpack Tuples Chapter.

## Video: Python Variable Names


---

# Python - Output Variables

## Output Variables

The print() function is often used to output variables.

```python
x = "Python is awesome"
print(x)
```

## Example

In the print() function, you output multiple 
variables, separated by a comma:

```python
x = "Python"y = "is"z = "awesome"print(x, y, z)
```

## Example

You can also use the + operator to output 
multiple variables:

```python
x = "Python "y = "is "z = "awesome"print(x 
  + y + z)
```

## Example

Notice the space character after "Python " and "is ",
  without them the result would be "Pythonisawesome".

For numbers, the + character works as a mathematical operator:

```python
x = 5y = 10print(x + y)
```

## Example

In the print() function, when you try to 
combine a string and a number with the + 
operator, Python will give you an error:

```python
x = 5y = "John"print(x + y)
```

## Example

The best way to output multiple variables in the print() function is to separate them with commas,
which even support different data types:

```python
x = 5y = "John"print(x, y)
```

## Example

## Video: Python Output Variables


---

# Python - Global Variables

## Global Variables

Variables that are created outside of a function (as in all of the examples 
in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of 
functions and outside.

```python
x = "awesome"
  def myfunc():  print("Python is " + x)myfunc()
```

## Example

Create a variable outside of a function, and use it inside the function

If you create a variable with the same name inside a function, this variable 
will be local, and can only be used inside the function. The global variable 
with the same name will remain as it was, global and with the original value.

```python
x = "awesome"
  def myfunc():  x = "fantastic"  print("Python is " + x)myfunc()
print("Python is " + x)
```

## Example

Create a variable inside a function, with the same name as the global 
  variable

## The global Keyword

Normally, when you create a variable inside a function, that variable is 
local, and can only be used inside that function.

To create a global variable inside a function, you can use the 
global keyword.

```python
def myfunc():  global x  x = "fantastic"myfunc()
print("Python is " + x)
```

## Example

If you use the global keyword, the variable belongs to the global scope:

Also, use the global keyword if you want to change a global variable inside a function.

```python
x = "awesome"def myfunc():  global x  x = "fantastic"myfunc()
print("Python is " + x)
```

## Example

To change the value of a global variable inside a function, refer to the 
  variable by using the global keyword:

## Video: Python Global Variables


---

# Python - Variable Exercises

## Test Yourself With Exercises

Now you have learned a lot about variables, and how to use them in Python.

Are you ready for a test?

Test your Python Variables skills with exercises from all categories:

## Exercises

Tip: Sign in to track your progress.

## Variables3 exercises

## Variable Names3 exercises

## Multiple Variable Values3 exercises

## Output Variable3 exercises

## Global Variable3 exercises

## Log in to track your progress

If you haven't already, sign up to become a W3Schooler, and get points for every exercise you complete.

As a logged-in W3Schools user you will have access to many features like having your own web page,
track your learning progress,
receive personal guided paths, and
more.

## The Exercise

The exercises are a mix of "multiple choice" and "fill in the blanks" questions.

There are between 3 and 9 questions in each category.

The answer can be found in the corresponding tutorial chapter.

If you're stuck, or answer wrong, you can try again or hit the "Show Answer" button to see the correct answer.

Find a complete collection of Python Exercises for each chapter in this tutorial in our Python Exercises page.


---

# Python Data Types

## Built-in Data Types

In programming, data type is an important concept.

Variables can store data of different types, and different types can do 
different things.

Python has the following data types built-in by default, in these categories:

Text Type: | str
Numeric Types: | int, float,
    complex
Sequence Types: | list, tuple, 
    range
Mapping Type: | dict
Set Types: | set, frozenset
Boolean Type: | bool
Binary Types: | bytes, bytearray, 
    memoryview
None Type: | NoneType

## Getting the Data Type

You can get the data type of any object by using the type() function:

```python
x = 5
print(type(x))
```

## Example

Print the data type of the variable x:

## Setting the Data Type

In Python, the data type is set when you assign a value to a variable:

Example | Data Type | Try it
x = "Hello World" | str | 
x = 20 | int | 
x = 20.5 | float | 
x = 1j | complex | 
x = ["apple", "banana", "cherry"] | list | 
x = ("apple", "banana", "cherry") | tuple | 
x = range(6) | range | 
x = {"name" : "John", "age" : 36} | dict | 
x = {"apple", "banana", "cherry"} | set | 
x = frozenset({"apple", "banana", "cherry"}) | frozenset | 
x = True | bool | 
x = b"Hello" | bytes | 
x = bytearray(5) | bytearray | 
x = memoryview(bytes(5)) | memoryview | 
x = None | NoneType | 

## Setting the Specific Data Type

If you want to specify the data type, you can use the following 
constructor functions:

Example | Data Type | Try it
x = str("Hello World") | str | 
x = int(20) | int | 
x = float(20.5) | float | 
x = complex(1j) | complex | 
x = list(("apple", "banana", "cherry")) | list | 
x = tuple(("apple", "banana", "cherry")) | tuple | 
x = range(6) | range | 
x = dict(name="John", age=36) | dict | 
x = set(("apple", "banana", "cherry")) | set | 
x = frozenset(("apple", "banana", "cherry")) | frozenset | 
x = bool(5) | bool | 
x = bytes(5) | bytes | 
x = bytearray(5) | bytearray | 
x = memoryview(bytes(5)) | memoryview | 


---

# Python Numbers

## Python Numbers

There are three numeric types in Python:

- int
- float
- complex

Variables of numeric types are created when you assign a value to them:

```python
x = 1    
  # inty = 2.8  # floatz = 1j   # complex
```

## Example

To verify the type of any object in Python, use the type() function:

```python
print(type(x))print(type(y))print(type(z))
```

## Example

## Int

Int, or integer, is a whole number, 
positive or negative, without decimals, of unlimited length.

```python
x = 1y = 35656222554887711z = 
  -3255522print(type(x))print(type(y))print(type(z))
```

## Example

Integers:

## Float

Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

```python
x = 1.10y = 1.0z = -35.59print(type(x))print(type(y))print(type(z))
```

## Example

Floats:

Float can also be scientific numbers with an "e" to indicate the power of 10.

```python
x = 35e3y = 12E4z = -87.7e100print(type(x))print(type(y))
  print(type(z))
```

## Example

Floats:

## Complex

Complex numbers are written with a "j" as the imaginary part:

```python
x = 3+5jy = 5jz = -5jprint(type(x))print(type(y))
  print(type(z))
```

## Example

Complex:

## Type Conversion

You can convert from one type to another with the int(), 
float(), and complex() methods:

```python
x = 1    # inty = 2.8  # floatz = 1j   # complex#convert from int to float:
  a = float(x)#convert from float to int:
  b = int(y)#convert from int to complex:c = complex(x)print(a)print(b)
  print(c)print(type(a))print(type(b))
  print(type(c))
```

## Example

Convert from one type to another:

Note: You cannot convert complex numbers into another number type.

## Random Number

Python does not have a random() function to 
make a random number, but Python has a built-in module called
random that can be used to make random numbers:

```python
import randomprint(random.randrange(1, 10))
```

## Example

Import the random module, and display a random number from 1 to 9:

In our Random Module Reference you will learn more about the Random module.


---

# Python Casting

## Specify a Variable Type

There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

- int() - constructs an integer number from an integer literal, a float literal (by removing 
    all decimals), or a string literal (providing the string represents a whole number)
- float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
- str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

```python
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
```

## Example

Integers:

```python
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
```

## Example

Floats:

```python
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
```

## Example

Strings:


---

# Python Strings

## Strings

Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:

```python
print("Hello")
print('Hello')
```

## Example

## Quotes Inside Quotes

You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

```python
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
```

## Example

## Assign String to a Variable

Assigning a string to a variable is done with the variable name followed by 
an equal sign and the string:

```python
a = "Hello"print(a)
```

## Example

## Multiline Strings

You can assign a multiline string to a variable by using three quotes:

```python
a = """Lorem ipsum dolor sit amet,consectetur adipiscing elit,sed do 
  eiusmod tempor incididuntut labore et dolore magna aliqua."""print(a)
```

## Example

You can use three double quotes:

Or three single quotes:

```python
a = '''Lorem ipsum dolor sit amet,consectetur adipiscing elit,sed do 
  eiusmod tempor incididuntut labore et dolore magna aliqua.'''print(a)
```

## Example

Note: in the result, the line breaks are inserted at the same position as in the code.

## Strings are Arrays

Like many other popular programming languages, strings in Python are arrays of unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

```python
a = "Hello, World!"
print(a[1])
```

## Example

Get the character at position 1 (remember that the first character has the 
position 0):

## Looping Through a String

Since strings are arrays, we can loop through the characters in a string, with a for loop.

```python
for x in "banana":  print(x)
```

## Example

Loop through the letters in the word "banana":

Learn more about For Loops in our Python For Loops chapter.

## String Length

To get the length of a string, use the len() function.

```python
a = "Hello, World!"
print(len(a))
```

## Example

The len() function returns the length of a string:

## Check String

To check if a certain phrase or character is present in a string, we can use 
the keyword 
in.

```python
txt = "The best things in life are free!"print("free" in txt)
```

## Example

Check if "free" is present in the following text:

Use it in an if statement:

```python
txt = "The best things in life are free!"if "free" in txt: 
print("Yes, 'free' is present.")
```

## Example

Print only if "free" is present:

Learn more about If statements in our Python 
If...Else chapter.

## Check if NOT

To check if a certain phrase or character is NOT present in a string, we can use 
the keyword not in.

```python
txt = "The best things in life are free!"print("expensive" not in txt)
```

## Example

Check if "expensive" is NOT present in the following text:

Use it in an if statement:

```python
txt = "The best things in life are free!"if "expensive" not in txt: 
print("No, 'expensive' is NOT present.")
```

## Example

print only if "expensive" is NOT present:


---

# Python - Slicing Strings

## Slicing

You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a 
part of the string.

```python
b = "Hello, World!"
  print(b[2:5])
```

## Example

Get the characters from position 2 to position 5 (not included):

Note: The first character has index 0.

## Slice From the Start

By leaving out the start index, the range will start at the first character:

```python
b = "Hello, World!"
  print(b[:5])
```

## Example

Get the characters from the start to position 5 (not included):

## Slice To the End

By leaving out the end index, the range will go to the end:

```python
b = "Hello, World!"
  print(b[2:])
```

## Example

Get the characters from position 2, and all the way to the end:

## Negative Indexing

```python
b = "Hello, World!"
  print(b[-5:-2])
```

## Example

Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):


---

# Python - Modify Strings

Python has a set of built-in methods that you can use on strings.

## Upper Case

```python
a = "Hello, World!"
print(a.upper())
```

## Example

The upper() method returns the string in upper case:

## Lower Case

```python
a = "Hello, World!"
print(a.lower())
```

## Example

The lower() method returns the string in lower case:

## Remove Whitespace

Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

```python
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
```

## Example

The strip() method removes any whitespace from the beginning or the end:

## Replace String

```python
a = "Hello, World!"
print(a.replace("H", "J"))
```

## Example

The replace() method replaces a string with another string:

## Split String

The split() method returns a list where the text between the specified separator becomes the list items.

```python
a = "Hello, World!"
print(a.split(",")) # 
  returns ['Hello', ' World!']
```

## Example

The split() method splits the string into substrings if it finds instances of the separator:

Learn more about Lists in our Python Lists chapter.

## String Methods

Learn more about String Methods with our String Methods Reference


---

# Python - String Concatenation

## String Concatenation

To concatenate, or combine, two strings you can use the + operator.

```python
a = "Hello"b = "World"c = a + b
print(c)
```

## Example

Merge variable a with variable 
b into variable c:

```python
a = "Hello"b = "World"c = a + " " + b
print(c)
```

## Example

To add a space between them, add a " ":


---

# Python - Format - Strings

## String Format

As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

```python
age = 36#This will produce an error:txt = "My name is John, I am " + ageprint(txt)
```

## Example

But we can combine strings and numbers by using f-strings or the format() method!

## F-Strings

F-String was introduced in Python 3.6,
and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string 
literal, and add curly brackets {} as 
placeholders for variables and other operations.

```python
age = 36txt = f"My name is John, I am {age}"print(txt)
```

## Example

Create an f-string:

## Placeholders and Modifiers

A placeholder can contain variables,
operations, functions, and modifiers to format the value.

```python
price = 59

txt = f"The price is {price} dollars"

print(txt)
```

## Example

Add a placeholder for the price variable:

A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like 
.2f which means fixed point number with 2 decimals:

```python
price = 59

txt = f"The price is {price:.2f} dollars"

print(txt)
```

## Example

Display the price with 2 decimals:

A placeholder can contain Python code, like math operations:

```python
txt = f"The price is {20 * 59} dollars"

print(txt)
```

## Example

Perform a math operation in the placeholder, and return the result:

Learn more about String Formatting in our String Formatting chapter.


---

# Python - Escape Characters

## Escape Character

To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

```python
txt = "We are the so-called "Vikings" from the north."
```

## Example

You will get an error if you use double quotes inside a string that is 
surrounded by double quotes:

To fix this problem, use the escape character \":

```python
txt = "We are the so-called \"Vikings\" from the north."
```

## Example

The escape character allows you to use double quotes when you normally would not be allowed:

## Escape Characters

Other escape characters used in Python:

Code | Result | Try it
\' | Single Quote | 
\\ | Backslash | 
\n | New Line | 
\r | Carriage Return | 
\t | Tab | 
\b | Backspace | 
\f | Form Feed | 
\ooo | Octal value | 
\xhh | Hex value | 


---

# Python - String Methods

## String Methods

Python has a set of built-in methods that you can use on strings.

Note: All string methods return new values. They do not change the original string.

Method | Description
capitalize() | Converts the first 
    character to upper case
casefold() | Converts string into 
    lower case
center() | Returns a centered 
    string
count() | Returns the number of 
    times a specified value occurs in a string
encode() | Returns an encoded 
    version of the string
endswith() | Returns true if the 
    string ends with the specified value
expandtabs() | Sets the 
    tab size of the string
find() | Searches the string for a 
    specified value and returns the position of where it was found
format() | Formats specified 
    values in a string
format_map() | Formats specified 
    values in a string
index() | Searches the string 
    for a specified value and returns the position of where it was found
isalnum() | Returns True if all 
    characters in the string are alphanumeric
isalpha() | Returns True if all 
    characters in the string are in the alphabet
isascii() | Returns True if all 
    characters in the string are ascii characters
isdecimal() | Returns True if all 
    characters in the string are decimals
isdigit() | Returns True if all 
    characters in the string are digits
isidentifier() | Returns True if 
    the string is an identifier
islower() | Returns True if all 
    characters in the string are lower case
isnumeric() | Returns True if 
    all characters in the string are numeric
isprintable() | Returns True if 
    all characters in the string are printable
isspace() | Returns True if all 
    characters in the string are whitespaces
istitle() | Returns True if the string follows the rules of a 
    title
isupper() | Returns True if all 
    characters in the string are upper case
join() | Joins the elements of 
    an iterable to the end of the string
ljust() | Returns a left justified 
    version of the string
lower() | Converts a string into 
    lower case
lstrip() | Returns a left trim 
    version of the string
maketrans() | Returns a 
    translation table to be used in translations
partition() | Returns a tuple 
    where the string is parted into three parts
replace() | Returns a string 
    where a specified value is replaced with a specified value
rfind() | Searches the string for 
    a specified value and returns the last position of where it was found
rindex() | Searches the string for 
    a specified value and returns the last position of where it was found
rjust() | Returns a right justified 
    version of the string
rpartition() | Returns a tuple 
    where the string is parted into three parts
rsplit() | Splits the string at 
    the specified separator, and returns a list
rstrip() | Returns a right trim 
    version of the string
split() | Splits the string at 
    the specified separator, and returns a list
splitlines() | Splits the string 
    at line breaks and returns a list
startswith() | Returns true if 
    the string starts with the specified value
strip() | Returns a trimmed version of the string
swapcase() | Swaps cases, lower 
    case becomes upper case and vice versa
title() | Converts the first 
    character of each word to upper case
translate() | Returns a 
    translated string
upper() | Converts a string 
    into upper case
zfill() | Fills the string with 
  a specified number of 0 values at the beginning


---

# Python - String Exercises

## Test Yourself With Exercises

Now you have learned a lot about Strings, and how to use them in Python.

Are you ready for a test?

## Exercises

Test your Python String skills with exercises from all categories:

## Strings

## Slicing Strings

## Modify Strings

## Concatenate Strings

## Format Strings

More Python Exercises:

Python Exercises


---

# Python Booleans

Booleans represent one of two values: 
True or False.

## Boolean Values

In programming you often need to know if an expression is 
True or False.

You can evaluate any expression in Python, and get one of two 
answers, 
True or False.

When you compare two values, the expression is evaluated and Python returns 
the Boolean answer:

```python
print(10 > 9)print(10 == 9)print(10 < 9)
```

## Example

When you run a condition in an if statement, Python returns 
True or False:

```python
a = 200b = 33if b > a:  print("b is greater than a")
  else:  print("b is not greater than a")
```

## Example

Print a message based on whether the condition is True or 
  False:

## Evaluate Values and Variables

The bool() function allows you to evaluate 
any value, and give you 
True or False 
in return,

```python
print(bool("Hello"))print(bool(15))
```

## Example

Evaluate a string and a number:

```python
x = "Hello"y = 15print(bool(x))print(bool(y))
```

## Example

Evaluate two variables:

## Most Values are True

Almost any value is evaluated to True if it 
has some sort of content.

Any string is True, except empty strings.

Any number is True, except 
0.

Any list, tuple, set, and dictionary are True, except 
empty ones.

```python
bool("abc")bool(123)bool(["apple", "cherry", "banana"])
```

## Example

The following will return True:

## Some Values are False

In fact, there are not many values that evaluate to
False, except empty values, such as (),
[], {}, 
"", the number
0, and the value None. 
And of course the value False evaluates to
False.

```python
bool(False)bool(None)bool(0)bool("")bool(())bool([])
  bool({})
```

## Example

The following will return False:

One more value, or object in this case, evaluates to 
False, and that is if you have an object that 
is made from a class with a __len__ function that returns 
0 or 
False:

```python
class myclass():  def __len__(self):    return 0
myobj = myclass()print(bool(myobj))
```

## Example

## Functions can Return a Boolean

You can create functions that returns a Boolean Value:

```python
def myFunction() :  return Trueprint(myFunction())
```

## Example

Print the answer of a function:

You can execute code based on the Boolean answer of a function:

```python
def myFunction() :  return Trueif myFunction():  
  print("YES!")else:  print("NO!")
```

## Example

Print "YES!" if the function returns True, otherwise print "NO!":

Python also has many built-in functions that return a boolean value, like the 
isinstance() 
function, which can be used to determine if an object is of a certain data type:

```python
x = 200print(isinstance(x, int))
```

## Example

Check if an object is an integer or not:


---

# Python Operators

## Python Operators

Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:

```python
print(10 + 5)
```

## Example

Although the + operator is often used to add together two values, like in the example above, it can also be used to add together a variable and a value, or two variables:

```python
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)
```

## Example

Python divides the operators in the following groups:

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators


---

# Python Arithmetic Operators

## Arithmetic Operators

Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator | Name | Example | Try it
+ | Addition | x + y | 
- | Subtraction | x - y | 
* | Multiplication | x * y | 
/ | Division | x / y | 
% | Modulus | x % y | 
** | Exponentiation | x ** y | 
// | Floor division | x // y | 

## Examples

Here is an example using different arithmetic operators:

```python
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
```

## Example

## Division in Python

Python has two division operators:

- / - Division (returns a float)
- // - Floor division (returns an integer)

```python
x = 12
y = 5

print(x / y)
```

## Example

Division always returns a float:

```python
x = 12
y = 5

print(x // y)
```

## Example

Floor division always returns an integer.

It rounds DOWN to the nearest integer:


---

# Python Assignment Operators

## Assignment Operators

Assignment operators are used to assign values to variables:

Operator | Example | Same As | Try it
= | x = 5 | x = 5 | 
+= | x += 3 | x = x + 3 | 
-= | x -= 3 | x = x - 3 | 
*= | x *= 3 | x = x * 3 | 
/= | x /= 3 | x = x / 3 | 
%= | x %= 3 | x = x % 3 | 
//= | x //= 3 | x = x // 3 | 
**= | x **= 3 | x = x ** 3 | 
&= | x &= 3 | x = x & 3 | 
|= | x |= 3 | x = x | 3 | 
^= | x ^= 3 | x = x ^ 3 | 
>>= | x >>= 3 | x = x >> 3 | 
<<= | x <<= 3 | x = x << 3 | 
:= | print(x := 3) | x = 3print(x) | 

## The Walrus Operator

Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:

```python
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")
```

## Example

The count variable is assigned in the if statement, and given the value 5:


---

# Python Comparison Operators

## Comparison Operators

Comparison operators are used to compare two values:

Operator | Name | Example | Try it
== | Equal | x == y | 
!= | Not equal | x != y | 
> | Greater than | x > y | 
< | Less than | x < y | 
>= | Greater than or equal to | x >= y | 
<= | Less than or equal to | x <= y | 

## Examples

Comparison operators return True or False based on the comparison:

```python
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
```

## Example

## Chaining Comparison Operators

Python allows you to chain comparison operators:

```python
x = 5

print(1 < x < 10)

print(1 < x and x < 10)
```

## Example


---

