# Problem 8 

''' input and prints the words in a comma-separated sequence after sorting
them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
Hints:
In case of input data being supplied to the question, it should be
assumed to be a console input.'''

items = [ x for x in input("Enter the the comma separated items.").split(',')]
items.sort()
print(','.join(items))
