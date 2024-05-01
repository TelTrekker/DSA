# DSA TASK 2

# MIclat, Shiela Mae    ACT-2


# VARIABLE ASSIGNMENTS

# Task: Create two variables, num1 and num2, and assign them integer values. Then, calculate their sum and store it in a variable called result.

num1: int = 5
num2: int = 3
result = num1 + num2
print(result)

# Task: Assign a string value to a variable called name. Then, print a message using the print() function that says "Hello, [name]!" where [name] is replaced with the value stored in the name variable.

name = 'Pogi'
print('Hello, ' + name + '!')


# GLOBAL AND LOCAL VARIABLES

# Task: Define a global variable global_var with a value of 10. Then, create a function local_function that defines a local variable local_var with a value of 5. Inside the function, print both global_var and local_var. Call the function and observe the output.

global_var: int = 10
def local_function (local_var=5):
    print(global_var + local_var)

local_function()

# Task: Create a function modify_global that attempts to change the value of global_var to 20. Call this function and print the value of global_var outside the function.
def modify_global():

    global global_var
    global_var = 20

modify_global()

print(global_var)


# ARITHMETIC OPERATORS

# TASK: Create two variables named num1 and num2, assign value to it. Write a function that takes two numbers from those variables and calculates their sum, difference, product, and quotient. Print the results.

num1 = 9
num2 = 8
def arithmetic():

    sum_result = num1 + num2
    diff_result = num1 - num2
    product_result = num1 * num2
    quotient_result = num1 / num2

    print(sum_result, diff_result, product_result, quotient_result)

arithmetic()

# TASK: Calculate the area of a triangle with a base of 8 units and a height of 6 units. Store the result in a variable called area and print it.

base = 8
height = 6

area = 0.5 * base * height
print(area)


# AUGMENTED ASSIGNMENT OPERATORS

# TASK: Initialize a variable count with the value 5. Use an augmented assignment operator to increment it by 3 and then multiply it by 2. Print the final value of count.

count = 5
count += 3
count *=2
print(f'Final count value: {count}')

# TASK: Create a variable price and set it to 100. Use an augmented assignment operator to decrease it by 20% to represent a discount. Print the discounted price.

price = 100
price *= 0.8
print(f'The discounted price is {price}')


# COMPARISON OPERATORS

# TASK: Compare two numbers, x and y (assign value of your choice), to check if x is greater than y. Print the result.

x = 7
y = 9
print(f'x > y: {x > y}')

# TASK: Compare two strings, str1 and str2 (assign value of your choice), to check if they are equal (case-sensitive). Print the result.

str1 = 'Porsche'
str2 = 'Mercedes'
print(f'str1==str2: {str1 == str2}')


# IN AND NOT IN OPERATORS

# TASK: Create a list of fruits. Use the in operator to check if "apple" is in the list.

fruits = ['coconut','watermelon','avocado','orange','apple']
print(f"'apple' in fruits {'apple' in fruits}")

# TASK: Create a string sentence and use the not in operator to check if "world" is not in the sentence. Print the result.

sentence = 'The Philippines is one of the Country for vacation around the world'
print(f"'world' not in sentence {'world' not in sentence}")


# LIST AND LIST MANIPULATION

# TASK: Create an empty list called my_list. Append three integers to it: 5, 10, and 15. Then, print the list.

my_list = []
my_list.append(5)
my_list.append(10)
my_list.append(15)
print(my_list)

# TASK: Given a list of numbers, numbers = [1, 2, 3, 4, 5], remove the last element using the appropriate list method. Print the modified list.

numbers = [1, 2, 3, 4, 5]
numbers.pop()
print(numbers)


# SUBLIST USING SLICES

# TASK: Create a list of numbers from 1 to 10. Use slicing to create a sublist containing elements from the 3rd to the 7th position (inclusive). Print the sublist.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sublist = numbers[2:8]
print(sublist)

# TASK: Given a string sentence (assign value to it, make sure it has "quick" word), use slicing to extract the word "quick" from it and print it.

sentence = 'assign value to it, make sure it has "quick" word'
word = sentence[37:45]
print(word)


# GETTING THE INDEX

# TASK: Create a list of colors. Find and print the index of the color "green" in the list

colors = ['blue','red','yellow','green']
print(f"index of 'green' in colors: {colors.index ('green')}")

# TASK: Create a list of fruits. Find and print the index of the color "mango" in the list.

fruits = ['orange','avocado','mango','dragonfruit']
print(f"index of 'mango' in fruits: {fruits.index ('mango')}")


# TUPLE

# TASK: Create a tuple named coordinates containing latitude and longitude values. Attempt to change one of the values in the tuple.

coordinates = (40.7128, -74.0060)

# TASK: Write a function (name is up to you) that returns a tuple containing the quotient and remainder when dividing two numbers. Call the function and print the result.

def divide_numbers(a, b):
    quotient = a // b
    remainder = a % b
    return (quotient, remainder)

result = divide_numbers(15, 4)
print(f"Quotient: {result[0]}, Remainder: {result[1]}")


# DICTIONARIES

# TASK: Create a dictionary representing a person's information with keys like "name," "age," and "city." Print the person's name from the dictionary.

person_info = {
    'name' : 'Dio Fab',
    'age' : 21,
    'city' : 'Igan'
}
print(f"persons_name: {person_info['name']}")

# TASK: Edit person's city. Print the dictionary.

person_info['city'] = 'Law'
print(person_info)


# RANGE() FUNCTION

# TASK: Use the range() function to create a sequence of numbers from 1 to 10 (inclusive). Print the numbers.

def function():

    for number in range (1, 11):
        print(number)

function()

# TASK: Create a list of even numbers from 2 to 20 using the range() function. Print the list.

even_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

even_numbers = list(range(2, 21, 2))
print(even_numbers)


# PRINT() FUNCTION

# TASK: Print the message "Hello, World!" using the print() function.

print('Hello World!')

# TASK: Create a list named fruits and assign values to it. Print the values of fruits separated by ','.

fruits = ['apple', 'orange', 'grapes', 'lemon']
print(', '.join(fruits))


# INPUT() FUNCTION

# TASK: Write a program that takes the user's name as input and prints a personalized greeting message.

user_name = input('Enter your name: ')
print(f'Hello {user_name} Thank You!')

# TASK:  Ask the user for two numbers and calculate their product. Print the result.

am1 = float(input('Please enter first amount: '))
am2 = float(input('Please enter second amount: '))
product = am1 * am2
print(f'The product is: {product}')


# LEN() FUNCTION

# TASK: Create a list of your favorite books. Use the len() function to find and print the number of books in the list.

favorite_books = ['48 Laws of Power', 'Atomic Habits', 'Influence: The Psychology of Persuasion', 'The Laws of Human Nature',
                  'Think and Grow Rich', 'The Way of the Superior Man', 'Zero to One', 'How to Win Friends and Influence People',
                  'The Psychology of Money', 'Meditations', 'The Elephant in the Brain', 'Art of War', 'Seduction', 'War',
                  'Mastery', 'Never Split The Difference']

print(f'Number of Favorite Books: {len(favorite_books)}')

# TASK: Get a user input sentence and calculate the number of characters in it using the len() function. Print the result.

user_input = input('Enter your favorite quote: ')
print(f'Number of characters: {len(user_input)}')


# CONTINUE / BREAK STATEMENTS

# TASK: Write a program that prints all the even numbers from 1 to 20 using a for loop. Use the continue statement to skip odd numbers.

print('Even numbers from 1 to 20: ')
for num in range (1, 21):
    if num % 2 != 0:
        continue
    print(num)
    continue

# TASK: Rewrite the same task above, but this time, if you reach 15, use break statement.

print('Even numbers from 1 to 20 with breaking point 15: ')
for num in range (1, 21):
    if num == 15:
        break
    if num % 2 != 0:
        continue
    print(num)


# WHILE AND FOR LOOPS

# TASK: Create a while loop that prints the numbers from 1 to 10.

print('Print numbers from 1 to 10: ')
count = 1
while count<= 10:
    print(count)
    count += 1

# TASK: Write a program that uses a for loop to iterate through a list of names and print each name with a greeting message.

names = ['Liza', 'Hope', 'Nancy', 'Sana']

for name in names:
    print(f'Hi {name}, I Love You!')


# WRITING FUNCTIONS

# TASK: Write a function add_numbers that takes two numbers as input and returns their sum. Call the function and print the result.
def add_numbers(a, b):
    return a + b

sum_result = add_numbers(9, 8)
print(f"Sum: {sum_result}")

# TASK: Create a function find_max that takes a list of numbers as input and returns the maximum value in the list. Call the function and print the result.

def find_max(numbers):
    return max(numbers)

max_value = find_max([17, 22, 8, 33, 28])
print(f"Maximum value: {max_value}")


#</>