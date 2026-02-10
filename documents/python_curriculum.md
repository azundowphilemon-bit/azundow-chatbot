# Python Curriculum

# Python Introduction

## Explanation
Python is a powerful, high-level programming language known for its simplicity and readability. It was created by Guido van Rossum and released in 1991.

### Key Features
- **Readable**: Uses English keywords and indentation.
- **Versatile**: Used in Web Development, Data Science, AI, Automation, and more.
- **Interpreted**: Code runs line-by-line, making debugging easier.

### Why Learn Python?
It's beginner-friendly but powerful enough for professionals at Google, NASA, and Netflix.

## Exercise
Write a Python command to print the text "Hello, Python!" to the screen.
```python
___("Hello, Python!")
```

---

# Python Syntax

## Explanation
Python syntax refers to the set of rules that defines how a Python program will be written and interpreted.

### Indentation
Unlike other languages that use curly braces `{}`, Python uses **indentation** (whitespace) to define blocks of code.
- Wrong Indentation = `IndentationError`.

### Example
```python
if 5 > 2:
    print("Five is greater than two!")  # This is indented
```

## Exercise
Fix the indentation in the following code:
```python
if True:
___print("This is indented correctly")
```

---

# Python Comments

## Explanation
Comments are lines that start with `#` and are ignored by Python. They are used to explain code or disable parts of it during testing.

### Single Line Comment
```python
# This is a comment
print("Hi")
```

### Multi-line Comment
Python doesn't have a specific multi-line comment syntax, but you can use triple quotes `"""` which act as multi-line strings (often used as docstrings).

## Exercise
Create a single-line comment that says "My Code".
```python
___ My Code
```

---

# Python Variables

## Explanation
Variables are containers for storing data values. In Python, you don't need to declare the type (e.g., `int x`). Python infers it automatically.

### Rules
- Must start with a letter or underscore `_`.
- Case-sensitive (`age`, `Age`, and `AGE` are different).
- Cannot contain spaces.

### Example
```python
x = 5           # Integer
y = "Hello"     # String
z = 3.14        # Float
```

## Exercise
Create a variable named `user_age` and set it to `25`.
```python
___ = 25
```

---

# Python Data Types

## Explanation
Every value in Python has a data type. Common types include:

- **Text**: `str` ("Hello")
- **Numeric**: `int` (10), `float` (10.5), `complex` (1j)
- **Sequence**: `list` ([1,2]), `tuple` ((1,2)), `range`
- **Mapping**: `dict` ({"name": "John"})
- **Set**: `set` ({1,2})
- **Boolean**: `bool` (True/False)

## Exercise
What is the data type of `x = 20.5`?
Options: `int`, `float`, `str`, `list`.

---

# Python Numbers

## Explanation
Python supports three numeric types:
1.  **int**: Whole numbers (e.g., `10`, `-5`).
2.  **float**: Decimal numbers (e.g., `10.5`, `-0.2`).
3.  **complex**: Numbers with an imaginary part (e.g., `2 + 3j`).

### Conversion (Casting)
You can convert types:
```python
x = 1    # int
y = float(x) # becomes 1.0
```

## Exercise
Convert the integer `5` to a float.
```python
num = 5
num_float = ___(num)
```

---

# Python Strings

## Explanation
Strings are surrounded by either single quotation marks or double quotation marks.

### F-Strings (Formatted Strings)
The modern way to format strings in Python 3.6+ is using `f-strings`.
```python
name = "Alice"
print(f"Hello, {name}!")
```

### String Methods
- `.upper()`: Converts to uppercase.
- `.lower()`: Converts to lowercase.
- `.strip()`: Removes whitespace from beginning/end.

## Exercise
Use an f-string to print "My name is [name]".
```python
name = "John"
print(f"My name is {___}")
```

---

# Python Booleans

## Explanation
Booleans represent one of two values: `True` or `False`.
They are often the result of comparisons.

### Example
```python
print(10 > 9)  # Returns True
print(10 == 9) # Returns False
```

### Truthiness
- Almost any value is evaluated to `True` if it has some content.
- Empty strings, `0`, `None`, and empty lists are `False`.

## Exercise
What will this print?
```python
print(5 > 10)
```
Options: `True`, `False`.

---

# Python Operators

## Explanation
Operators perform operations on variables and values.

### Arithmetic
`+`, `-`, `*`, `/`
`%` (Modulus - Remainder)
`**` (Exponentiation - Power)
`//` (Floor Division - Integer result)

### Logical
`and`, `or`, `not`

### Example
```python
x = 5
print(x > 3 and x < 10) # True
```

## Exercise
Use the multiplication operator to multiply 5 by 2.
```python
print(5 ___ 2)
```

---

# Python Lists

## Explanation
Lists are used to store multiple items in a single variable. Types **List** items are ordered, changeable, and allow duplicate values.

### Creating a List
```python
fruits = ["apple", "banana", "cherry"]
```

### Accessing Items
Lists are 0-indexed.
```python
print(fruits[0]) # apple
```

## Exercise
Print the last item in the list `numbers = [10, 20, 30]`.
```python
numbers = [10, 20, 30]
print(numbers[___])
```

---

# Python Tuples

## Explanation
A Tuple is a collection which is ordered and **unchangeable**.
Written with round brackets `()`.

### Example
```python
thistuple = ("apple", "banana", "cherry")
```
Once created, you cannot change, add, or remove items.

## Exercise
Create a tuple with one item "apple". (Hint: needs a comma!)
```python
mytuple = ("apple"___)
```

---

# Python Sets

## Explanation
A Set is a collection which is unordered, unchangeable*, and unindexed.
*Items are unchangeable, but you can add/remove items.
No duplicate members allowed.
Written with curly brackets `{}`.

### Example
```python
myset = {"apple", "banana", "cherry"}
```

## Exercise
Add "orange" to the set.
```python
fruits = {"apple", "banana"}
fruits.___("orange")
```

---

# Python Dictionaries

## Explanation
Dictionaries store data values in `key:value` pairs.
Ordered (as of Python 3.7), changeable, and no duplicates.
Written with curly brackets `{}`.

### Example
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
```

## Exercise
Change the "year" to 2020.
```python
car = {"brand": "Ford", "year": 1964}
car["year"] = ___
```

---

# Python If...Else

## Explanation
Python supports logical conditions: `==`, `!=`, `<`, `>`, `<=`, `>=`.

### Syntax
```python
if condition:
    # code
elif other_condition:
    # code
else:
    # code
```

### Short Hand
```python
print("Yes") if 5 > 2 else print("No")
```

## Exercise
Print "Yes" if `a` is equal to `b`.
```python
a = 50
b = 50
if a ___ b:
  print("Yes")
```

---

# Python While Loops

## Explanation
With the `while` loop we can execute a set of statements as long as a condition is true.

### Example
```python
i = 1
while i < 6:
  print(i)
  i += 1 # Remember to increment i, or the loop will continue forever.
```

## Exercise
Stop the loop if `i` is 3.
```python
i = 1
while i < 6:
  if i == 3:
    ___
  i += 1
```

---

# Python For Loops

## Explanation
A `for` loop is used for iterating over a sequence (list, tuple, string, etc.).

### Range
`range(start, stop, step)` function returns a sequence of numbers.
```python
for x in range(6):
  print(x) # 0 to 5
```

## Exercise
Loop through the list `fruits`.
```python
fruits = ["apple", "banana"]
for x ___ fruits:
  print(x)
```

---

# Python Functions

## Explanation
A function is a block of code which only runs when it is called.
Defined using the `def` keyword.

### Arguments
Information can be passed into functions as arguments.
```python
def my_function(fname):
  print(f"Hello {fname}")
```

### Return Values
To let a function return a value, use the `return` statement.

## Exercise
Create a function named `my_function`.
```python
___ my_function():
  print("Hello")
```

---

# Python Lambda

## Explanation
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

### Syntax
`lambda arguments : expression`

### Example
```python
x = lambda a : a + 10
print(x(5))
```

## Exercise
Create a lambda function that adds `a` and `b`.
```python
x = lambda a, b : a ___ b
```

---

# Python Classes/Objects

## Explanation
Python is an Object Oriented Language.
Almost everything in Python is an object, with its own properties and methods.

### Create a Class
```python
class MyClass:
  x = 5
```

### The __init__() Function
All classes have a function called `__init__()`, which is always executed when the class is being initiated.

## Exercise
Create a class named `Person`.
```python
___ Person:
  name = "John"
```

---

# Python Inheritance

## Explanation
Inheritance allows us to define a class that inherits all the methods and properties from another class.

- **Parent class** is the class being inherited from, also called base class.
- **Child class** is the class that inherits from another class, also called derived class.

## Exercise
Create a class `Student` that inherits from `Person`.
```python
class Student(___):
  pass
```

---

# Python Iterators

## Explanation
An iterator is an object that contains a countable number of values.
Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods `__iter__()` and `__next__()`.

## Exercise
Return an iterator from a tuple.
```python
mytuple = ("apple", "banana", "cherry")
myit = ___(mytuple)
```

---

# Python Scope

## Explanation
A variable is only available from inside the region it is created. This is called **scope**.

### Local Scope
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

### Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

## Exercise
The variable `x` created inside a function is available where?
Options: `Inside function only`, `Global scope`.

---

# Python Modules

## Explanation
Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.

### Import
Use the `import` keyword to make the code in a module available.

## Exercise
Import the module named `mymodule`.
```python
___ mymodule
```

---

# Python Dates

## Explanation
A date in Python is not a data type of its own, but we can import a module named `datetime` to work with dates as date objects.

### Example
```python
import datetime

x = datetime.datetime.now()
print(x)
```

## Exercise
Import the datetime module and display the current date:
```python
import ___
x = datetime.datetime.now()
print(x)
```

---

# Python Math

## Explanation
Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

### Built-in
`min()` and `max()` functions.
`abs()` returns absolute (positive) value.

### Math Module
`import math`
`math.sqrt(64)` returns 8.0.

## Exercise
Use the correct method to find the square root of 64.
```python
import math
x = math.___(64)
```

---

# Python JSON

## Explanation
JSON is a syntax for storing and exchanging data.
Python has a built-in package called `json`, which can be used to work with JSON data.

### Parse JSON
Convert from JSON to Python:
```python
import json
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])
```

## Exercise
Parse 'x' (which is JSON string) to a Python dictionary.
```python
import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.___(x)
```

---

# Python RegEx

## Explanation
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
Python has a built-in package called `re`.

### Example
```python
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
```

## Exercise
Import the re module.
```python
import ___
```

---

# Python PIP

## Explanation
PIP is a package manager for Python packages, or modules if you like.
It is used to install and manage software packages written in Python.

### Install
`pip install camelcase`

### Uninstall
`pip uninstall camelcase`

## Exercise
What is the correct syntax to install a package named "camelcase"?
```python
pip ___ camelcase
```

---

# Python Try Except

## Explanation
The `try` block lets you test a block of code for errors.
The `except` block lets you handle the error.
The `else` block lets you execute code when there is no error.
The `finally` block lets you execute code, regardless of the result of the try- and except blocks.

### Example
```python
try:
  print(x)
except:
  print("An exception occurred")
```

## Exercise
In the example below, the `try` block will generate an error, because x is not defined. Complete the `except` block.
```python
try:
  print(x)
___:
  print("An exception occurred")
```

---

# Python User Input

## Explanation
Python allows for user input.
That means we can ask the user for input.
The method is a bit different in Python 3.6 than Python 2.7.
Python 3.6 uses the `input()` method.

### Example
```python
username = input("Enter username:")
print("Username is: " + username)
```

## Exercise
Use the correct method to ask the user for input.
```python
x = ___("Type your name:")
```

---

# Python String Formatting

## Explanation
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
```python
age = 36
txt = "My name is John, I am " + age
print(txt)
```

But we can combine strings and numbers by using f-strings or the `format()` method!

### F-String (Preferred)
```python
age = 36
txt = f"My name is John, I am {age}"
```

## Exercise
Use the correct syntax to format the string.
```python
price = 49
txt = f"The price is {___} dollars"
```
