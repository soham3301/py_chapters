import random

the_ran_no = round(random.random() * 100)
if the_ran_no <= 50:
    print("It's a tail")
else:
    print("It's a head")

# Another way

rand_no_2 = random.randint(0, 1)
if rand_no_2 == 1:
    print("It's a HEAD")
else:
    print("It's a TAIL")