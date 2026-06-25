import random

friends = ["Soham", "Joy da", "Amitav", "Payel", "Amitav er bou"]

random_number = random.randint(0, 4)

print(f"Bill will be paid by {friends[random_number]}")

# Another way to do it

the_person = random.choice(friends)
print(f"Bill will be paid by {the_person}")