# Range function has to work with another function.

# The Gauss Challenge
counter = 0
for target in range(1, 101):
    counter += target
print(counter)

# range(start, stop, steps)

for target in range(15):            #   <--- range(stop) with one argument
    print(target)

for target in range(0, 15):         #   <--- range(start, stop) with two argument
    print(target)

for target in range(0, 15, 3):      #   <--- range(start, stop, steps) with three arguments
    print(target)