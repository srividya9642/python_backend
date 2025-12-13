# Nested Dictionaries : A dictionary can contain dictionaries, this is called nested dictionaries.


# create a dictionary that containg three dictionaries":

myfamily = {
    'child1': {
    'name' : 'Emily',
    'year' : 2004
        
    },
    "child2" : {
    'name' : 'Tobias',
    'year' : 2007
    },
    'child3' : {
    'name' : 'Linus',
    'year' : 2011
    }
}

print(myfamily)

# if we want to add three dictionaries into a new dictionary:

child1 = {
    'name' : 'Emil',
    'year' : 2004
}
child2 = {
    'name' : 'Tobias',
    'year' : 2007
}
child3 = {
    'name' :'Linus',
    'year' : 2011
}

myfamily = {
    'child1' : child1,
    'child2' : child2,
    'child3' : child3

}

print(myfamily)

# Access items in Nested Dictionaries.
''' To access items from a nested dictionary, we use the name of the dictionaries, 
starting with the outer dictionary:'''

# Example : print the name of child2 :

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily['child2']['name'])


# Loop through the nested dictionaries : we can loop through a dictionary by using the items() method like this.abs

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])

