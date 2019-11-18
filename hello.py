print("Hello, World!")
fred = '''What time is it? It is 11:49.
What time does the next bus departs? I don't know.'''
print(fred)

myscore = 1000
message = 'I scored %s points.'
print(message % myscore)

joke_text = '%s: a device for finding furniture in the dark'
bodypart1 = 'Knee'
bodypart2 = 'Shin'
print(joke_text % bodypart1)
print(joke_text % bodypart2)

nums = 'What did the number %s said to the number %s? Nice belt!'
print(nums % (0, 8))
# What did the number 0 said to the number 8? Nice belt!

print(10 * 'a' + 'h')
# aaaaaaaaaah

# LIST
wizard_list = ['spider legs', 'toe of frog', 'eye of newt',
               'bat wing', 'slug butter', 'snake danddruff']
print(wizard_list)
# ['spider legs', 'toe of frog', 'eye of newt', 'bat wing',
# 'slug butter', 'snake danddruff']
print(wizard_list[2])
# eye of newt
wizard_list[2] = 'snail tongue'
print(wizard_list[2:5])
wizard_list.append('bear burp')
print(wizard_list)
del wizard_list[5]
print(wizard_list)

some_numbers = [1, 2, 5, 10, 20]
some_strings = ['Which', 'Witch', 'Is', 'Which']
numbers_and_strings = ['Why', 'was', 6, 'afraid', 'of', 7,
                       'because', 7, 8, 9]
mylist = [some_numbers, some_strings]
# mylist has two elements.

list1 = [1, 2, 3, 4]
list2 = ['I', 'tripped','over', 'and', 'hit', 'the', 'floor']
# joining lists (concatenate)
print(list1 + list2)
list3 = list1 + list2
print(list3)
# repeat list
list4 = [0, 1]
print(list4 * 5)

# TUPLE
fibs = (0, 1, 1, 2, 3)
print(fibs[3])

# MAP or DICT (dictionary)
favorite_sports = {'Ralph Williams' : 'Football',
                'Michael Tippett' : 'Basketball',
                'Edward Elgar' : 'Baseball',
                'Rebecca Clarke' : 'Netball',
                'Ethel Smyth' : 'Badminton',
                'Frank Bridge' : 'Rugby'}
print(favorite_sports['Rebecca Clarke'])
del favorite_sports['Ethel Smyth']
favorite_sports['Ralph Williams'] = 'Ice Hockey'

# TURTLE




