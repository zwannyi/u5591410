#Loop Through a Dictionary
#You can loop through a dictionary by using a for loop.

#Print all key names in the dictionary, one by one:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 2024
}
for x in thisdict:
  print(x)

  #Print all values in the dictionary, one by one:
  thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 2024
}
for x in thisdict:
  print(thisdict[x])

#You can also use the values() method to return values of a dictionary:
  thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 2024
}
for x in thisdict.values():
  print(x)

#You can use the keys() method to return the keys of a dictionary:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 2024
}
for x in thisdict.keys():
  print(x)


#Loop through both keys and values, by using the items() method:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 2024
}
for x, y in thisdict.items():
  print(x, y)

#Copy a Dictionary
#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

#There are ways to make a copy, one way is to use the built-in Dictionary method copy().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2024
}
mydict = thisdict.copy()
print(mydict)

#Another way to make a copy is to use the built-in function dict().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2024
}
mydict = dict(thisdict)
print(mydict)


#A dictionary can contain dictionaries, this is called nested dictionaries.
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

#Or, if you want to add three dictionaries into a new dictionary:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}