import random

friends = ["Soham", "Joy da", "Amitav", "Payel", "Amitav er bou"]

print(len(friends))                                         #   <--- This will output the whole length

random_number = random.randint(0, len(friends) - 1)         #   <--- The minus one is needed. (Length == Index - 1)

print(f"Bill will be paid by {friends[random_number]}")

# Another way to do it

the_person = random.choice(friends)
print(f"Bill will be paid by {the_person}")