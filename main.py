import re  # regex


# Types
print("Aloha!")
print(5+6)
print("5"+"6")
print(2.73*3.14)
print(int("5")+int("7"))
print('She said: "I want that."')
print('She said: "Don\'t do that."')
print("This costs " + str(6+5) + " dollars.")
print("My name is " + "Hello:Angela:Nick".split(":")[1])
# string = str
# integer = int
# float = float
# boolean = bool

# Boolean operations
print(5 == 5)
print(5 == 4)
print(5 is not 4)
print(5 is 4)
print("This" is "This")
print("True" is True)
print("True" is str(True))

# Lists (arrays)

print("I like " + ["barbecue", "movies", "pizza"][1])

# Dictionaries
print({"name": "Angela", "age": 32, "hobby": "code"}["name"])

# Variables
greeting = "Hello World"
print(greeting)
print(greeting.split(" ")[0])


# Built-in functions

# len(): returns the length of an array of characters
# in a string.

# sorted(): sort elements.

# User defined functions

def my_function(str1, str2):
    print(str1)
    print(str2)

my_function("This is arg 1", "This is arg 2.")
my_function("String", "Hello, World!")


# Default arguments

def print_something(name="Someone", age="Unknown"):
    print("My name is", name, "and my age is", age)

print_something("Angie")


# Keyword arguments

print_something(age="27", name="Angie")


# Infinite arguments

# * tells this argument is going to be an array.
def print_people(*people):
    for person in people:
        print("This person is", person)

print_people("Nick", "Dan", "Angie", "Dani")


# Return values from functions

def do_math(num1, num2):
    return num1 + num2

math1 = do_math(5, 7)
math2 = do_math(11, 34)

print("First sum is", math1, "and the second sum is", math2)


# Conditional statements
# if, elif, else

check = "Hamburger"

if check == "False":
    print("It is false")
elif check == "Hamburger":
    print("Yummm, hamburgers")
elif check == "Yo":
    print("Hello")
else:
    print("It is actually equal to True")

# for/while loops

numbers = [1, 2, 3, 4]

for item in numbers:
    print(item)

run = True
current = 1

while run:
    if current == 10:
        run = False
    else:
        print(current)
        current += 1

# Import libraries to a script

string = "'I AM NOT YELLING', she said. Though " \
         "we knew it to not be true."
print(string)
new = re.sub('[a-z]', '', string)
print(new)
new = re.sub('[A-Z]', '', string)
print(new)
new = re.sub('[.,\']', '', string)
print(new)
new = re.sub('[.,\'a-zA-Z]', '', string)
print(new)
new = re.sub('[.,\'A-Z+" "]', '', string)
print(new)
string = string + "1+2 - 100"
print(string)
# ^ means exception
new = re.sub('[^0-9]', '', string)
print(new)
