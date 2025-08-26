#Variables
from operator import truediv

name = "Taran"
age = "17"

#Expressions and statements:

name = "Taran"; print(name)

#Comments
# Using a hashtag allows you to place comments around your code that does not clash with your code

#Data types

name = "Taran"
print(type(name)) # return str
print(type(name) == str) # return true
print(isinstance(name, str)) # return true true

age = 17
print(isinstance(age, int)) # return true true
print(isinstance(age, float)) # return true false

number = float(17)
print(isinstance(number, float)) # return true true

    #complex for complex numbers
    #bool for booleans
    #list for lists
    #tuple for tuples
    #range for ranges
    #dict for dictionaries
    #set for sets

#Arithmetic Operators
1 + 1 #2
2 - 1 #1
2* 2 #4
4 / 2 #2
4 % 3 #1
4 ** 2 #16
4 // 2 #2

print("Scamp" + "is a good dog") #Combing string with arithmetic operator

age = 8
age += 8 # age = age + 8  can do with any other operator
print(age)

#Comparison operators
a = 1
b = 2
a == b #False
a != b #True
a > b #False
a <= b #True

#Boolean operators

condition1 = True
condition2 = False

not condition1 #False
condition1 and condition2 #False
condition1 or condition2 #True

print(0 or 1) ## 1
print(False or 'hey' ) ## 'hey'
print( 'hi' or 'hey' ) ## 'hi'
print([] or False) ## 'False'
print(False or []) ## '[]']

#Bitwise operators

    # & - performs binary AND
    # | - performs binary OR
    # ^ - performs a binary XOR operation
    # ~ - performs a binary NOT operation
    # << - shift left operation
    # >> - shift right operation

#Is and in operator

    # is
    # in

#Ternary operator

def is_adult(age):
    if age > 18:
        return True
    else:
        return False #Slow way - no ternary operator

def is_adut2(age):
    return True if age > 18 else False #Fast way - Ternary operator

#String

"Taran"

'Taran'

name = "Taran"

phrase = name + "is my name"

name = "Taran"
name += "is my name"

age = str("17")

#String methods

print("Taran".upper())

print("Taran".lower())

print("Taran".title()) #Capatilse the first letter of the word within the print

print("taran".islower) #True or false weather word is all lower, print True

print("TARAN".isupper) #True or false weather word is all upper, print True


    #print("person".islower())
    #isalpha() to check if a string contains only characters and is not empty
    #isalnum() to check if a string contains characters or digits and is not empty
    #isdecimal() to check if a string contains digits and is not empty
    #lower() to get a lowercase version of a string
    #islower() to check if a string is lowercase
    #upper() to get an uppercase version of a string
    #isupper() to check if a string is uppercase
    #title() to get a capitalized version of a string
    #startsswith() to check if the string starts with a specific substring
    #endšwith() to check if the string ends with a specific substring
    #replace() to replace a part of a string
    #split() to split a string on a specific character separator
    #strip() to trim the whitespace from a string
    #join() to append new letters to a string
    #find() to find the position of a substring

#String characters and slicing

name = "Taran"
print(name[0]) #Will print the first letter of my name
print(name[-1]) #Will print the last letter of my name
print(name[0:2]) #Will print the first two letters of my name (Ta)
print(name[:4]) #Will print everything before the fourth index
print(name[4:]) #Will print everything after the fourth index

#Boolean

    #Have two values - True or False

done = True
#done = False
#done = 1
#done = 0 #All numbers are True except for 0 which is always False

print(type(done) == bool) #Checks weather done is bool. whcih will print True as it is

if done:
    print("yes")
else:
    print("no") #Will print yes as done is stated as True

book_1_read = True
book_2_read = False
read_any_book = any([book_1_read, book_2_read]) #Will print true as the 'any' functions checks at least one variable is True

#Number data types

num1 = 2 + 3j
num2 = complex(2,3)
print(num2.real, num2.imag)

#Built-in functions

print(abs(-5.5))
print(round(5.5))
print(round(-5.5,1))

#Enums

from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])
print(State['ACTIVE'].value)
print(list(State))
print(len(State))

#User input

age = input("What is your age?")
print("Your age is" + age)

#Control statements
condition = True

if condition == True:

    print("The condition")
    print("was true")

print("Outside if")

#Lists

dogs = ["Roger", 1, "Syd", True, "Quincy", 7]

dogs[2] = "Beau" #Alters item on list
print(dogs[2:4])

print("Roger" in dogs) #Print True
print("Bradley" in dogs) #Print False

#dogs.append("Judah") #Adds item to a list
#dogs.extend(["Judah", 5])
dogs += ["Judah", 5]

dogs.remove("Quincy") #Remove items on a list

print(dogs.pop()) #Removes last item on a list

print(dogs)

items = ["Roger", 1, "Syd", True, "Quincy", 7]

items.insert(2, "Test")

items[1:1] = ["Test1", "Test2"]

print(items)

#Sorting lists

items = ["Roger", "George", "Syd", "Bradley", "Quincy", "Beau", "bob"]

items.sort(key = str.lower)
print(items)

#Tuples

names = ("Roger", "Syd")

names[-1]
names.index("Roger")

len(names)

print("Roger" in names)
names[0:2]

newTuple = names + ("Tina", "Quincy")

#Dictionaries

dog = { "name" : "Roger" , "age" : 8, "colour": "green" }

print(dog["name"])

#dog["name"] = "Syd"

#print(dog.get("name"))
#print(dog.get("color", "brown")) #Only return brown if colour is not in dictionary

#print(dog.pop("name"))

print(dog.popitem())

print("colour" in dog)

print(dog.keys())
print(list(dog.keys()))
print(list(dog.values()))

print(dog)

#Sets

set1 = {"Roger", "Syd"}
set2 = {"roger", "lunar"}

intersect = set1 & set2 # give the items found in both sets
mod = set1 | set2 #Gives item in both set

mod = set1 > set2 #checks eather set 1 has the same items in set 2, False
mod = set1 < set2 #checks eather set 1 has the same items in set 2, True

print(mod)

#Functions

def hello1(name = "my friends"):
    print("Hello!" + name)

hello1("Beua")
hello1("Quincy")
hello1()

def hello2(name, age):
    print("Hello!" + name + "you are" + str(age) + "years old")

hello2("Taran", 17)

#Variable scope

age = 8 #Global variable

def test():
   # age = 8 #Local variable
    print(age)


print(age)
test()

#Nested function

def talk(phrase):
    def say(word):
        print(word)

    words = phrase. split(' ')
    for word in words:
        say(word)

talk('I am going to buy the milk')

def count( ):
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()

count ()

#Closures
def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count
    return increment

increment = counter()

print(increment())
print(increment())
print(increment())

#Objects

age = 8

print(age.real)
print(age.imag)
print(age.bit_length())


items = [1, 2]
items.append(3)
items.pop()
print(id(items))


#Loops

condition = True
while condition == True:
    print("The condition is True")
    condition = False

count = 0
while count < 10:
    print("The condition is True")
    count = count + 1

print("After the loop")

items = [1,2,3,4]
for item in items:
    print(item)

items = [1,2,3,4]
for index, item in enumerate(items):
    print(index, item)

#Break and continue

items = [1,2,3,4]
for items in items:
    if item == 2:
        continue
        print(item)

items = [1,2,3,4]
for items in items:
    if item == 2:
        break
        print(item)

#Classes

class Animal:
    def walk(self):
        print("Walking...")



class Dog(Animal):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

roger = Dog("Roger", 8)

print(roger.name)
print(roger.age)

roger.bark()
roger.walk()

#Modules

#Arguments form command line

import sys

name = sys.argv[1]

print("Hello" + name)

import argparse

parser = argparse.ArgumentParser( description = "This program prints the name of my dogs")

parser. add_argument('-c', ' -- color', metavar='colour',
required=True, choices = {'red', 'yellow'}, help='the color to search for')

args = parser.parse_args ()

print(args.colour)

#Lambda functions

lambda num : num * 2

multiply = lambda a, b : a * b

print(multiply(2, 4))

#Map, Filter, Reduce

    #numbers = [1,2,3,4,5,6]
    #result = map(lambda a: a * 2, numbers) #Using map
    #result = filter(lambda num: num % 2 == 0, numbers) #using filter
    #print(list(result))

    #from functools import reduce

    #expenses = [
        #('Dinner', 80)
        #('Car repair', 120)
    #]

    #sum = reduce(lambda a, b: a[1] + b[1], expenses) #Using reduce
    #print(sum)

#Recursion

def factorial(n):
        if n == 1: return 1
        return n * factorial(n - 1)

print(factorial(3))
print(factorial(4))
print(factorial(5))

#Decorators

def logtime(func):
    def wrapper():
        print("before")
        val=func() #Allows hello to be but in the middle of before and after
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("Hello")

hello()

#Docstrings

def increment(n):
    """Increment a number"""
    return n + 1

class Dog:
    def __init__(self, name, age):
        """Initialize a Dog object"""
        self.name = name
        self.age = age

    def bark(self):
        """Let the dog bark"""
        print("WOOF!")

#Annotations

def increment(n: int) -> int:
    return n + 1

count: int = 0

#Exceptions

#try
#except <ERROR1>: # Has to be a specific error, just an example
#except <ERROR2>: # Has to be a specific error, just an example
#except:

try:
    result = 2 / 0
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    result = 1
print(result)

#try:
    #raise exception('An error') #general exception
#except Exception as error:
    #print(error)

#With

filename = '/Users/flavio/test.txt'

try:
    file = open(filename, 'r')
    content = file. read( )
    print(content)
finally:
    file.close()

with open(filename, 'r') as file:
    content = file.read()
    print(content)

#Third party packages - pip

    #Install pip
        #Go to terminal and write 'pip install request

    #Unintall pip
        #Go to terminal and write 'pip uninstall request'

#List compression

numbers = [1,2,3,4,5]

numbers_power_2 =  [n**2 for n in numbers]

print(numbers_power_2)

number_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)

numbers_power_2 = list(map(lambda n : n**2, numbers)) #This way is alot more complex compared to the other after the first line

#Polymorphism

class Dog:
    def eat(self):
        print( 'Eating dog food' )

class Cat:
    def eat(self):
        print( 'Eating cat food' )

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()

#Operator overloading

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return True if self.age > other.age else False

roger = Dog("Roger", 8)
syd = Dog("Syd", 7)

print(roger > syd) #Return true as roger is older
print(syd > roger) #Return false as roger is older

    #__add__() respond to the + operator
    #__sub__() respond to the - operator
    #__mul__() respond to the * operator
    #__truediv__() respond to the / operator
    #__floordiv__() respond to the // operator
    #__mod__() respond to the % operator
    #__pow__() respond to the ** operator
    #__rshift__() respond to the >> operator
    #__lshift__() respond to the << operator
    #__and__() respond to the & operator
    #__or__() respond to the | operator
    #__xor__() respond to the ^ operator