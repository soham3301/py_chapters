# small pizza = $15
# medium pizza = $20
# large pizza = $25

# add pepperoni for small pizza = +$2
# add pepperoni for medium or large pizza = +$3

# extra cheese for any size pizza = +$1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? s, m, or l ")
add_pepperoni = input("Do you want pepperoni? y or n ")
extra_cheese = input("Do you want extra cheese? y or n ")

#Initialising the bill
bill = 0

#Setting the price according to their sizes
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
     print("You entered the size wrong")

#Setting the price if pepperoni added or not
if add_pepperoni == "y":
    if size == "s":
         bill += 2
    elif size == "m" or size == "l":
         bill += 3

if extra_cheese == "y":
        bill += 1

print(f"Your final bill is ${bill}")

