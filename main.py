import math

# Lesson 1

    # print("Barlykov Beket")
    # print('o----')
    # print(' ||||')
    # print('*' * 10)
    # print('|' * 2 + '-' * 3 + '@' * 4)
    # print('1' * 1 + '2' * 2 + '3' * 3)

# lesson 2 variables

        # price = 100 # assigning an integer value to the variable price
        # price = 200 # reassigning a new integer value to the variable price
        # rating = 5.1 # float value
        # print(price) # printing the value of the variable price

        # name = "Beket" # string type
        # is_published = False # boolean type

    # Simple exercise to define a patient John Smith, age 20 and he is a new patient

        # patient_fullname = "John Smith" # assigning name of the patient to the variable patient_fullname, string type
        # patient_age = 20 # assigning the age of the patient to the variable patient_age, integer type
        # is_patient_new = True # indicating that the John Smith is the new patient by assigning the variable is_patient_new with boolean True

# Lesson 3 Getting input

        # my_name = input('What is your name? ') # input function prints on the console message in the brackets/parantheses and waits for the input from the console to be entered and assigns the entered value to the variable my_name
        # print('Hi, ' + my_name)

    # Simple exercise. Ask two questions: person's name and favourite color. Then, print a message like "Beket likes black color"

        # name = input('What is your name? ')
        # color = input('What color do you like? ')

        # print(name + ' likes ' + color + ' color')

# Lesson 4 Type Conversion

    # Simple program that asks for a birth year and prints the possible age according to the birth year

        # birth_year = input('Which year were you born? ') # whenever you use an input function, its input value will be str (string) type
        # print(type(birth_year))
        # age = 2020 - int(birth_year) # in order to calculate the age you need to convert str value of birth_year variable into integer by using int(birth_year) function
        # print(type(age))
        # print(age)

    # Simple task. Ask a use their weight (in pounds), convert it to kilograms and print on the terminal.

        # weight_in_pounds = input('How much you weight in pounds? ') # asks for the user the weight in pounds
        # weight_in_kg = 0.453592 * float(weight_in_pounds) # converts the str type of the variable 'weight_in_pounds' to float and then converts the pound value of pounds to kg
        # print(weight_in_kg) # print the value of the variable 'weight_in_kg tj the terminal

# Lesson 5 Strings

    # course = "'Python's Course for Begginers" # single quotes inside of double quotes
    # new_course = 'Python Course for "Begginers"' # double quotes inside of single quotes
    # multi_line_string = '''
    # Hi, Beket,
    # Here is the message that tells you that you are
    # AMAZING
    # ''' # 3 single quotes that are used to multi line strings

    # course1 = 'Python for Beginners' # the concept in which string is defined as a array of characters
    # print(course1[0]) # this function prints the first character of the string variable course1
    # print(course1[-1]) # the negative one index is the index of the last character and index 0 is the index of the first character
    # print(course1[-2]) # -2 index is the second character from the end
    # print(course1[0:3]) # index [0:3] prints the characters from index 0 inclusively to index 3 exclusively
    # print(course1[0:]) # index [0:] prints all characters starting from index 0 to the end of the string
    # print(course1[1:]) # index [1:] prints all characters starting from index 1 to the end of the string
    # print(course1[:5]) # index [:5] prints all characters from the start till the index 5 exclusively
    # print(course1[:]) # index [:] prints all the characters in the string

    # another = course1[:] # this statement assigns all characters of str variable course1 to the variable another
    # print(another) # prints str variable another

# name = 'Beket'
# print(name[1:-1]) # prints all characters from index 1 included to the index -1 which is the last character of the string excluded

# Lesson 6 Formatted Strings

    # first_name = 'Beket'
    # last_name = 'Barlykov'
    # message = first_name + ' [' + last_name + '] is a coder'
    # msg = f'{first_name} [{last_name}] is a coder' # formatted string,
    # with curly brackets we define placeholder or holes in our string msg,
    # this holes will be filled values of our variables first_name and last_name
    # print(msg)

# Lesson 7 String methods

    # course = 'Python for Beginners'
    # print(len(course)) # string method len() indicates the length of the string variable
    # len() general purpose function

    # print(course)

    # print(course.upper())
    # course.upper() is a method specifically for string variables
    # that changes all characters in a string variable to upper case characters

    # print(course.lower())
    # course.lower() is a method
    # that prints a new string from course string variable with all lower characters

    # print(course.find('P'))
    # course.find(str) is a method that searches
    # for the first occurence of the soecific attribute character in a string variable
    # and returns its index
    # .find method is case sensitive and if there is no character defined in the attribute it returns -1

    # print(course.replace('Beginners', 'Absolute Begginers'))
    # .replace(str, str) is a method that replaces the character or sequence of characters with a new character or sequence of characetrs in the string variable

    # print('Python' in course)
    # 'Python' in course is a statement that searchs for a specific character or a sequence of characters
    # and returns boolean True if it exists in the string variable
    # or False if does not exists in the string variable

# Lesson 8 Arithemtic Operations

    # print(10 + 3) # addition
    # print(10 - 3) # substraction
    # print(10 * 3) # multiplication
    # print(10 / 3) # floating point division
    # print(10 // 3) # integer division
    # print(10 % 3) # modulus that returns remainder of division
    # print(10 ** 3) # power, 10 ** 3 = 1000

    # x = 10
    # x = x + 3
    # x += 3 # augmented assignment operator
    # x -= 3
    # x *= 3
    # print(x)

# Lesson 9 Operator precedence

    # parenthesis
    # 2 ** 3 exponentiation \
    # ~ + - complement, unary plus or minus
    # * / % // multiplication, division, modulo, floor division
    # + - addition or substraction
    # >> <<	Right and left bitwise shift
    # &	Bitwise 'AND'td>
    # ^ |	Bitwise exclusive `OR' and regular `OR'
    # <= < > >=	Comparison operators
    # <> == !=	Equality operators
    # = %= /= //= -= += *= **=	Assignment operators
    # is is not	Identity operators
    # in not in	Membership operators
    # not or and	Logical operators

# Lesson 10 Math Functions

    # round(x)
    # round(float) function to the closest integer value

    # abs(-2.9)
    # abs() function returns absolute value of the number

    # To use complex mathematical functions
    # we should import math module of python
    # import math

    # math.ceil(2.9)
    # math.ceil(float) rounds to the top integer of a number

    # floor(2.9)
    # floor(float) rounds to the bottom integer of a number

# Lesson 11 If statements

    # is_hot = False
    # is_cold = False

    # if is_hot:
    #    print("It's a hot day")
    #    print("Drink plenty of water")
    #elif is_cold: # elif = else if
    #    print("It's a cold day")
    #    print("Wear warm clothes")
    #else:
    #    print("It's a lovely day") # to close if statement you need to press SHIFT + TAB
    #print("Enjoy your day")

# Simple exercise: Price of a house is 1M
#if a buyer has good credit
#   they need to put down 10%
# Otherwise
#   they need to put down 20%
# Print the down payment

    #credit = input("Is your credit good?")
    #is_credit_good = False
    #house_price = 1000000

    #if credit == 'Yes':
     #   is_credit_good = True
    #else:
     #   is_credit_good = False

    #if is_credit_good == True:
    #    house_price = house_price * 0.1
    #else:
    #    house_price = house_price * 0.2

    #print(f"Down payment: ${house_price}")

# Lesson 12 Logical Operators

# AND: both conditions should be true
# OR: at least one should be true
# NOT: Changes True to False and vice versa

    #if applicant has high income AND good credit
    # Eligible for loan

        #has_high_income = True
        #has_good_credit = True

        #if has_high_income and has_good_credit:
        #print("Eligible for loan")

    #if applicant has high income OR good credit
    # Eligible for loan
        #has_high_income = True
        #has_good_credit = False

    # if has_high_income or has_good_credit:
    #    print("Eligible for loan")


    #if applicant has good credit AND doesn't have a criminal record
    # Eligible for loan

        #has_good_credit = True
        #has_criminal_record = True

        #if has_good_credit and not has_criminal_record:
        #    print("Eligible for loan")

# Lesson 13 Comparison operators

#If temperature is greater than 30
# it's a hot day
#otherwise if it's less than 10
# it's a cold day
#otherwise
# it's neither hot nor cold

    #temperature = 30

    #if temperature > 30:
    #    print("It's a hot day")
    #elif temperature < 10:
    #    print("It a cold day")
    #else:
    #    print("it's neither hot nor cold")

    # Simple exercise:
    # if name is less than 3 characters long
    #   name must be at least 3 characters
    # otherwise if it's more than 50 characters long
    #   name can be a maximum of 50 characters
    #otherwise
    #   name looks good

    #name = input("Input a name: ")

    #if len(name) < 3:
    #    print("name must be at least 3 characters")
    #elif len(name) > 50:
    #    print("name can be a maximum of 50 characters")
    #else:
    #    print("name looks good")

    # Simple exercise 2
        #weight = input("Weight: ")
        #unit = input("(L)bs or (k)g: ")
        #is_lbs = False

        #if unit.upper() == "L":
        #    is_lbs = True
        #else:
        #    is_lbs = False

        #if is_lbs:
        #    weight = float(weight) * 0.45
        #    print(f"You are {weight} kg")
        #else:
        #    weight = float(weight) * 2.2
        #   hel print(f"You are {weight} pounds")

# Lesson 14 While loops

# while condition:
#   ...

    # i = 1
    # while i <= 5:
    #     print('*' * i)
    #     i += 1
    # print("Done")

# Exercise 1 Guessing Game

    # secret_number = 9
    # guess_count = 0
    # guess_limit = 3
    #
    # while guess_count < guess_limit:
    #     guessed_number = int(input("Guess: "))
    #     if guessed_number == secret_number:
    #         print("You won")
    #         break # break statement stops a loop
    #     guess_count += 1
    # else: # while loop can also have else part
    #     print("You have failed")

# Exercise 2 Car game

    # car = '>'
    # command = ""
    # is_car_start = False
    # is_car_stop = False
    #
    #
    # while True:
    #     print(car)
    #     command = input("")
    #     if command.upper() == "HELP":
    #         print('''
    # start - to start the car
    # stop to stop the car
    # quit - to exit
    #         ''')
    #     elif command.upper() == "START" and is_car_start == False:
    #         is_car_start = True
    #         print("Car started... Ready to go!")
    #     elif command.upper() == "START" and is_car_start == True:
    #         print("Car already started.")
    #     elif command.upper() == "STOP" and is_car_stop == False:
    #             is_car_stop = True
    #             print("Car stopped.")
    #     elif command.upper() == "STOP" and is_car_stop == True:
    #         print("Car already stopped.")
    #     elif command.upper() == "QUIT":
    #         break
    #     else:
    #         print(f"I don't understand that...")

# Lesson 15 For Loops
#Iterate over each character in a string, array

    # for item in 'Python':
    #     print(item) # This for loop will iterate over string 'Python' and print every character in a new line
    # for item in ['Beket', 'Aset', 'Medeu']: # This for loop will iterate over list of name and print each name in a new line
    #     print(item)
    # for item in [1, 2, 3, 4]: # This for loop iterates over the list of numbers and prints each nymber in a new line
    #     print(item)

    # for item in range(10): # range function range(int) creates an object that we can iterate over
    #     print(item)

    # for item in range(5, 10): # range function range(int, int) creates an object from first int to second int range that we can iterate over
    #     print(item)

    # for item in range(1, 11, 2): # range function(int1, int2, int3) creats an list kind of object starting from number int1 to number int 2 (exclusively) and step int3
    #     print(item)

# Simple exercise: to calculate total cost of all the items in a shooping cart
#     prices = [10, 20, 30]
#     total = 0
#
#     for price in prices:
#         total += price
#
#     print(total)

# Lesson 16 Nested Loops
# Loop inside of another loop
# List of coordinates

    # for x in range(4): # outer loop, iteration of x
    #     for y in range(3): # inner loop, iteration of y
    #         print(f"({x}, {y})") # print each iteration

# Challenge Exercise
    # xxxxx
    # xx
    # xxxxx
    # xx
    # xx
    #
    # numbers = [5, 2, 5, 2, 2]
    # My solution:
    #     for i in numbers:
    #         j = i
    #         while j != 0:
    #             print('x', end = '')
    #             j -= 1
    #         print('')
    # MOsh's solution
    #     for x_count in numbers:
    #         output = ''
    #         for count in range(x_count):
    #             output += 'x'
    #         print(output)

# Lesson 17 Lists

    # names = ['Beket', 'Aset', 'Medeu', 'Elmira', 'Amangali']
    # names[0] = 'Krasavchik'
    # print(names[0])
    # #print(names[-5])
    # # print(names[:])

# Simple exercise:  Write a program to find the largest number in a list
    # numbers = [32, 54, 76, 150, 23, 53, 31]
    # max = 0
    #
    # for number in numbers:
    #     if max < number:
    #         max = number
    #
    # print(max)

# Lesson 18 2D lists
    # 2D list is a list where each element of the list is another list

    # matrix = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]
    # # print(matrix[0][1])
    # # Nested loops are used to iterate over each element in 2D list
    # for row in matrix:
    #     for item in row:
    #         print(item)

# Lesson 19 List Methods

    # numbers = [2, 5, 5, 6, 2, 4, 6, 7, 9, 8, 9]

    # numbers.append(3) # .append(object) is a method to add element to the end of the list
    # numbers.insert(0, 10) # .insert(int, object) is a method to insert element at the specific index
    # numbers.remove(10) # .remove(object) removes specific element from the list
    # numbers.clear() # .clear() is a method that removes all element from the list
    # numbers.pop() # .pop() removes last item from the list
    # print(numbers.index(5)) # .index(object) check the index of the specific element in the list and returns it, but if there is no such element in the list, it returns ValueError
    # print(2 in numbers) # "object in list" checks whether specific element exists in a list and returns boolean value True if exists and False if does not
    # print(numbers.count(2)) # .count(object) returns the number of times the specific element exists in a list
    # numbers.sort() # .sort() is a method that sorts elements by ascending order in a list but returns None value if printed
    # numbers.reverse() # .reverse() is a method that reverses elements in a list and changes their indexes. This method with .sort() method are used to sort the list in Descending order: firstly, you sort using .sort() method and then .reverse() method
    # numbers2 = numbers.copy() # .copy() copies a list
    # print(numbers2)

# Simple exercise: Write a program to remove the duplicates in a list
    # for item in numbers:
    #     if numbers.count(item) > 1:
    #         numbers.remove(item)
    # print(numbers)

# Lesson 20 Tuples
# Important structure similar to lists
# cant modify them, only get information

    # # numbers = [1, 2, 3] # Square brackets define lists
    # numbers = (1, 2, 3) # Parenthesis define tuples
    #
    # # numbers.count() # .count() to count number of occurences of an item
    # # numbers.index() # .index() to return the index of the first occurence of an item
    #
    # # Similar to lists, we can access individual items in the tuple
    # # numbers[0] = 10 # if you try to change the item in the tuple, you will get TypeError
    # print(numbers[0])

# Lesson 21 Unpacking
# powerful feature of Python

    # coordinates = [1, 2, 3]
    #     # x = coordinates[0]
    #     # y = coordinates[1]
    #     # z = coordinates[2]
    #
    # x, y, z = coordinates # each item in a tuple or a list is assigned to a variable by order
    # print(y)

# Lesson 22 Dictionaries
    # Name: Beket
    # Email: beket@gmail.com
    # Phone: 1234

    # customer = { # Dictionaries are defined using a pair of curly brackets
    #     "name": "Beket Barlykov",
    #     "age": 20,
    #     "is_verified": True
    # }
    # # customer["name"] = "Aset Barlykov" # you can modify the values of a key in a dictionary
    # print(customer["name"]) # can access dictionaries using square brackets and key like "name"
    # print(customer["birthdate"]) # if accessing the dictionary using a key that does not exists like "birthdate", we get KeyError
    # print(customer.get("birth", "Aug 21 2000")) # we can also access dictionary using .get("key") method, and if you access non existing key using .get() method it does not show KeyError, it returns  "None"
    # customer["birthdate"] = "September 15 2002" # you can also add new key with its value to dictionary

# Simple exercise: type a phone number in digits and it will translate it into the words

    # digits = {
    #     "+": "Plus",
    #     "0": "Zero",
    #     "1": "One",
    #     "2": "Two",
    #     "3": "Three",
    #     "4": "Four",
    #     "5": "Five",
    #     "6": "Six",
    #     "7": "Seven",
    #     "8": "Eight",
    #     "9": "Nine"
    # }
    # phone = input("Phone: ")
    # count = 0
    # while count < len(phone):
    #     print(digits[phone[count]], end = ' ')
    #     count += 1

# Lesson 23 Emoji converter

    # message = input(">")
    # words = message.split(' ') # .split(str) method that searches for a specific string and uses it as a boundary to separate each string in a list
    # emojis = {
    #     ":)":  "😀",
    #     ":(":  "😥"
    # }
    # output = ""
    # for word in words:
    #     output += emojis.get(word, word) + " "
    #
    # print(output)

# Lesson 24 Functions

    # def greet_user():
    #     print("Hi there")
    #     print("Welcome aboard")
    #
    #
    # print("Start")
    # greet_user()
    # print("Finish")

# Lesson 25 Parameters

    # def greet_user(first_name, last_name):
    #     print(f'Hi, {first_name} {last_name}!')
    #     print("Welcome aboard")
    #
    #
    # print("Start")
    # greet_user("Beket", "Barlykov")
    # print("Finish")

# Lesson 26 Keyword Arguments
# With keyword arguments we dont have to worry about the order of the arguments
    # def greet_user(first_name, last_name):
    #     print(f'Hi, {first_name} {last_name}!')
    #     print("Welcome aboard")
    #
    #
    # print("Start")
    # greet_user(last_name = "Barlykov", first_name = "Beket")
    # print("Finish")
    # calc_cost(total = 50, shipping = 5, discount = 0.1) # improves readibility of the code by using keyword arguments

# Lesson 27 return statement
# All functions in Python returns None
    # def square(number):
    #     return number ** 2
    #
    #
    # print(square(99))

# Lesson 28 Creating a Resuable Function

    # def emoji_converter(message):
    #     words = message.split(' ') # .split(str) method that searches for a specific string and uses it as a boundary to separate each string in a list
    #     emojis = {
    #         ":)":  "😀",
    #         ":(":  "😥"
    #     }
    #     output = ""
    #     for word in words:
    #         output += emojis.get(word, word) + " "
    #     return output
    #
    #
    # message = input(">")
    # print(emoji_converter(message))

# Lesson 29 Exceptions
# How to handle errors in Python
    # try:
    #     age = int(input('Age: ')) # if a user enters non numberical symbols, exception error will occur
    #     income = 20000
    #     risk = income / age
    #     print(age)
    # except ZeroDivisionError: # this exception catches the ZeroDivisionError when user enters 0 as an inpit for age
    #     print('Age cannot be 0')
    # except ValueError:  # this line will catch that exception and we define what should happen if ValueError appears
    #     print('Invalid value')

# Lesson 30 Comments
    #  bvkadfbkvabbk
    # print('Sky is blue')

# Lesson 31 Classes

    # numbers = [1, 2, 3]
    # # new defined class point
    # class Point:
    #     def move(self):
    #         print("move")
    #
    #     def draw(self):
    #         print("draw")
    #
    #
    # point1 = Point() #defining object
    # #defining attributes
    # point1.x = 10
    # point1.y = 20
    # print(point1.x)
    #
    # point2 = Point()
    # point2.x = 1
    #
    #
    # point1.draw()
    # point1.move()

# Lesson 32 Constructors
# Construction is a function that gets called in the time of creating an object
    # class Point:
    #     def __init__(self, x, y): # (constructor) init is a function or method that gets called when we create a new point object
    #         self.x = x # reference to the current object
    #         self.y = y
    #     def move(self):
    #         print("move")
    #
    #     def draw(self):
    #         print("draw")
    #
    # point = Point(10, 20)
    # print(point.x)

# Simple exercise:
# Define a new type called Person:
# - name attribute
# - talk() method

    # class Person:
    #     def __init__(self, name):
    #         self.name = name
    #     def talk(self):
    #         print(f'Hi, {self.name}')
    #
    #
    # person1 = Person("Beket Barlykov")
    # person1.talk()
    # print(person1.name)
    #
    # person2 = Person("Aset Barlykov")
    # person2.talk()

# Lesson 33 Inheritance
# mechanism of reusing code
# DRY = Don't repeat yourself
    # class Mammal:
    #     def walk(self):
    #         print("walk")


    # class Dog(Mammal): # DOg class will inherit all methods from parent class Mammal
    #     def bark(self):
    #         print("barl")
    #
    #
    # class Cat(Mammal):
    #     def be_annoying(self):
    #         print("annoying")
    #
    #
    # dog1 = Dog()
    # dog1.walk()
    #
    # cat1 = Cat()
    # cat1.walk()

# Lesson 34 Modules
# file with some pyhton code
# use modules to better organize your code
    # import converter # importing the whole module converter
    # from converter import kg_to_lbs # importing specific function kg_to_lbs from module converter
    #
    # kg_to_lbs(72) # when we import only specific function from the module we can use this function without it's prefixe module name
    #
    # print(converter.kg_to_lbs(70))
    # print(converter.lbs_to_kg(160))

# Simple exercise:
# find the largest number in the list using functions and the place it in different pyhon file for module
# there is a built-in function in Python called max() to find the largest number in list or tuple
    # import utils
    #
    # numbers = [51, 32, 68, 12, 42, 98]
    #
    # print(utils.find_max(numbers))

# Lesson 35 Packahes
# Package is a container for multiple modules
# It is better to organize big number of python files into packages
    # import ecommerce.shipping # to import module from another package we need to prefix the module with the name of the package that module is located in
    # # when working with packages it is better to use from package.module import function() type of import
    # # because you dont have to write prefixes all the time
    # from ecommerce.shipping import calc_shipping
    # # you can also import the whole module from the package
    # from ecommerce import shipping
    # ecommerce.shipping.calc_shipping()

# Lesson 36 Generating Random Values
# built-in modules in Python for generating random values
# several libraries for different purposes
    # import random

    # for i in range(2):
    #     print(random.random()) # random.random() generates random float value from 0 to 1
    #     print(random.randint(10, 20)) # random.randint(int1, int2) generates a random integer number in range from int1 to int2

    # members = ['Beket', 'Aset', 'Medeu', 'Mama', 'Papa']
    # leader = random.choice(members) # random.choice(list) is a method to randomly pick an element from the list
    # print(leader)

# Simple exercise:
# write a program that rolles a 2 dices
    #
    # class Dice:
    #     def roll(self):
    #         dice1 = random.randint(1, 6)
    #         dice2 = random.randint(1, 6)
    #         return (dice1, dice2)
    #
    #
    # dice = Dice()
    # print(dice.roll())

# Lesson 37 Files and Directories
# pathlib object oriented filesystem paths
# from pathlib import Path
# Absolute path: Root of hard disk: c:\Program Files\ Microsoft
# Relative path

    # print(path.mkdir()) # path.mkdir(str) is a method shortened from make directory, makes new directory with a name
    # path.rmdir() is a function that removes or deletes directory
    # print(path.exists("emails")) # path.exists() returns boolean value True if this directory or file exists and False if not
    #  path.glob() method are used to search for files and directories
    # path.glob('*') searches for all files and directories
    # path.glob('*.*') searches only all files but not for directories
    # *.py will search for all .py Python files
    # *.xls will search for all .xls Excel files

# path = Path()
# for file in path.glob('*.py'): # path.glob('*.7
#     print(file)
# for file in path.glob('*'):
#     print(file)

# Lesson 38 PyPi and Pip
# pypi.org you can find thousand of Python   packages
# openpyxl 3.0.5

# import openpyxl as xl # as xl is used to prefix not by typing openpyxl by just xl
# from openpyxl.chart import BarChart, Reference # classes to create Bar charts
#
#     # accessing cell A1 by referencing to its cell index
#     # cell = sheet1['a1']
#     # accessing cell A1 by referencing to (row, column) coordinates of cell
#     # cell1 = sheet1.cell(1, 1)
#     # cell.value is used to retrieve the  value inside the cell
#     # print(cell.value)
#     # .max_row is used to retrieve the max number of rows in the sheet
#     # print(sheet1.max_row)
#
# def process_workbook(filename):
#     # loading transactions.xlsx Excel file and assigning into the variable wb
#     wb = xl.load_workbook(filename)
#     # accessing first sheet of Excel file
#     sheet1 = wb['Sheet1']
#
#     for row in range(2, sheet1.max_row + 1):
#         # assign to cell variable cells of iterating row and third column
#         cell = sheet1.cell(row, 3)
#         corrected_price = cell.value * 0.9
#         # save values of corrected price at next column 4
#         corrected_price_cell = sheet1.cell(row, 4)
#         corrected_price_cell.value = corrected_price
#
#     values = Reference(sheet1,
#               min_row = 2,
#               max_row = sheet1.max_row,
#               min_col = 4,
#               max_col = 4)
#
#     bar_chart = BarChart() # creating an bar_chart constructor of BarChart
#     bar_chart.add_data(values) # adding values to bar_chart
#     sheet1.add_chart(bar_chart, 'e2') # inserting bar_chart into cell E2
#     # save the changes in a excel file
#     wb.save(filename)

# Project 2: Machine Learning with Python
# Steps in Machine LearningL
#   1. Import the Data
#   2. Clean the data
#   3. Split the Data into Training/Test Sets
#   4. Create a Model
#   5. Train the Model
#   6. Make Predictions
#   7. Evaluate and Improve
# Libraries and Tools for MAchine Learning:
    # 1. Numpy
    # 2. Pandas
    # 3. MatPlotLib
    # 4. Scikit-Learn
    
# Importing a Data Set

# Project 3: Building a website with DJango
# Framework is a library of reusable modules(building blocks)
# A framework defines a structure for our applications

