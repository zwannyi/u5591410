#can change the value of a specific item by referring to its key name:
#Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020
}
thisdict["year"] = 2024

#The update() method will update the dictionary with the items from the given argument.
#Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020
}
thisdict.update({"year": 2024})

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2024
}
thisdict["color"] = "red"
print(thisdict)

#The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

#Add a color item to the dictionary by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2024
}
thisdict.update({"color": "red"})

#Removing Items
#There are several methods to remove items from a dictionary:
#The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2024
}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2024
}
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2024
}
del thisdict["model"]
print(thisdict)

#The clear() method empties the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2024
}
thisdict.clear()
print(thisdict)
