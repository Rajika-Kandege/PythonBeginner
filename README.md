

# Python Basics

# What is __init__?
 
The __init__ method is a special method in Python classes, commonly known as the constructor. It is automatically called when an instance of the class is created. This method is used to initialize the attributes of the class

# What does self mean?
  
self is a reference to the current instance of the class. It is used to access variables that belong to the class. It allows each instance of the class to keep track of its own attributes and methods

# What does an object refer to?
  
An object is an instance of a class. In Python, everything is an object, including numbers, strings, functions, and classes. An object is a collection of data (variables) and methods (functions) that act on the data

# Formatted Strings with print(f"")

 Formatted string literals (also known as f-strings) provide a way to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and formatted using the str.format() method.

# Classes and Objects

 A class is a blueprint for creating objects. Classes encapsulate data for the object and methods to manipulate that data. An object is an instance of a class  

# Defining Methods

Methods are functions defined within a class that describe the behaviors of the objects created from the class

# Instantiating Objects

To create an instance of a class (i.e., an object), you call the class using its name and pass any required parameters.  

# Indentation
  
Python uses indentation to indicate a block of code. Indentation is crucial in Python as it defines the level of nesting of statements. It typically consists of four spaces or a tab.

# Docstring

Added a docstring to the method to describe its purpose

# The in Operator

The in operator in Python is used to check if a value is present in a sequence (such as a string, list, tuple, or dictionary). It returns True if the value is found and False otherwise  
# Naming Conventions
  
Naming conventions are important in Python to ensure your code is readable and maintainable. Here are some common conventions:

File Names: File names should be all lowercase with words separated by underscores (e.g., my_module.py).

Class Names: Class names should use the CapWords convention (also known as CamelCase). 
Each word should start with a capital letter, and no underscores should be used (e.g., MyClass).

Method and Function Names: Method and function names should be all lowercase with words separated by underscores (e.g., my_function or my_method).

Variable Names: Variable names should be all lowercase with words separated by underscores (e.g., my_variable).

# The sorted Function

In Python, the sorted function is used to sort iterables like lists, tuples, and dictionaries. It returns a new sorted list while leaving the original iterable unchanged. The sorted function accepts an iterable as its argument and returns a sorted list.

# The min and max Functions

In Python, the min and max functions are used to find the minimum and maximum values, respectively, from an iterable (such as a list, tuple, or dictionary).

# The min Function

The min function returns the smallest element from the iterable.

# The max Function

The max function returns the largest element from the iterable.

# Slicing

 The notation [::] is called slicing in Python. Slicing is a powerful feature that allows you to extract a subset of elements from an iterable, such as a list, tuple, or string, based on specified indices or step values.

When using slicing with just colons (:), it has the following format:

[start:stop:step]

Here's what each part means:

start: The index where the slice starts (inclusive). If not specified, it defaults to the beginning of the iterable.
stop: The index where the slice ends (exclusive). If not specified, it defaults to the end of the iterable.
step: The step size or the increment by which the elements are selected. If not specified, it defaults to 1.
So, when you see [::], it's a shorthand way of specifying a slice that includes all elements of the iterable, starting from the beginning, ending at the end, and with a step size of 1.

When you want to reverse a list using slicing, you can use [::] with a negative step size, which means you start from the end and go towards the beginning. For example, [:: -1] reverses the list.
