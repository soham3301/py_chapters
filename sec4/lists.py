cities = ["Dharmanagar", "Kailashahar", "Ambassa", "Khowai", "Agartala", "Bishalgarh", "Udaipur", "Belonia"]

print(cities[1])
print(cities[-3])
print(cities[1:4])

# Changing one item with another

cities[4] = "Dhaleshwar"
print(cities)

# Adding one name in the list

cities.append("Kamalpur")
print(cities)

cities.insert(0, "Gondacherra")     #   <--- inserting into specific index
print(cities)

# Removing name from list

cities.pop()                        #   <--- removing the last item | .pop(index) could be possible
print(cities)

cities.remove("Dhaleshwar")
print(cities)

# nested lists
districts = ["West", "Sepahijala", "Khowai", "Gomati", "South", "Dhalai", "Unakoti", "North"]
whole_tripura = [cities, districts]

print(whole_tripura[1][1])