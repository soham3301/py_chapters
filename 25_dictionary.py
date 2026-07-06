
#* ==================================================BASICS====================================================================
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

getting_all_keys = car.keys()           #!  <<< Getting all the KEYS
getting_all_values = car.values()       #!  <<< Getting all the VALUES
getting_items_as_tuples = car.items()   #!  <<< Getting all items as Tuples

print(getting_all_values)               #?  <<< Print

get_method = car.get("model")           #!  <<< Getting the VALUE, needs the Key
using_keys = car["year"]

car["color"] = "black"                  #!  <<< Adding

car["year"] = 1969                      #!  <<< Updating

car.update({"model": "Shelby"})         #!  <<< This Updates
car.update({"type": "4WL"})             #!  <<< This Changes

print(car)                              #?  <<< Print

car.pop("color")                        #!  <<< Needs Keys to remove the pair
del car["brand"]                        #!  <<< Same as .pop("key")     |||         WARNING:-   del can completely delete the whole dict.

print(car)                              #?  <<< Print

car.popitem()                           #!  <<< Removes the last item

car.clear()                             #!  <<< Completely emptying the dict

print(car)                              #?  <<< Print

#* ===================================================LOOPS===================================================================

my_details = {
    "first_name": "Soham",
    "second_name": "Datta",
    "age": 34,
    "mobile": 8787692757,
    "address": {
        "road": "Mohanpur",
        "town": "Kamalpur",
        "dist": "Dhalai",
        "state": "Tripura"
    }
}

for my_keys in my_details:                                  #!  <<< looping and getting all the KEYS
    print(f"My KEYS: {my_keys}")

for my_values in my_details:                                #!  <<< looping and getting all the VALUES
    print(f"My VALUES: {my_details[my_values]}")

for my_all_keys in my_details.keys():                       #!  <<< another way to loop and get KEYS
    print(my_all_keys)

for my_all_values in my_details.values():                   #!  <<< another way to loop and get VALUES
    print(my_all_values)

for x, y in my_details.items():                             #!  <<< looping through keys and values TOGETHER
  print(x, y)

#!  Copying the dictionary
copy_of_my_details = my_details.copy()
another_copy_of_my_details = dict(my_details)

#!  NESTED in a new way

friend1 = {
    "name": "Amitava",
    "age": 34
}

friend2 = {
    "name": "Souvik",
    "age": 32
}

friend3 = {
    "name": "Akash",
    "age": 33
}

my_friends = {
    "first_one": friend1,
    "second_one": friend2,
    "third_one": friend3
}

for keys, values in my_friends.items():
    for exact_keys, exact_value in values.items():
        print(exact_keys, ":", exact_value)
        # print(exact_value)
        # print(exact_value, ":", values[exact_value])


#* ===================================================METHODS===================================================================

#? clear()	Removes all the elements from the dictionary
#! copy()	Returns a copy of the dictionary
#? fromkeys()	Returns a dictionary with the specified keys and value
#! get()	Returns the value of the specified key
#? items()	Returns a list containing a tuple for each key value pair
#! keys()	Returns a list containing the dictionary's keys
#? pop()	Removes the element with the specified key
#! popitem()	Removes the last inserted key-value pair
#? setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#! update()	Updates the dictionary with the specified key-value pairs
#? values()	Returns a list of all the values in the dictionary
