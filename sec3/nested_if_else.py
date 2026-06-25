print("=======================================")
print("Welcome to the rollercoaster!!")
print("=======================================")

height = int(input("What is your height in cm?\n"))

if height > 120:
    age = int(input("What is your age?\n"))
    need_pic = input("Do you want a picture? (y / n)\n")

    if age <= 12:
        if need_pic == "y":
            ride_fee_child = int(input("Pay $8\n"))
            if ride_fee_child >= 8:
                print("Yes, Enjoy your ride WITH PICTURE kiddo.")
            else:
                print(f"Sorry, You paid ${ride_fee_child} which is less than $8")
        else:
            ride_fee_child = int(input("Pay $5\n"))
            if ride_fee_child >= 5:
                print("Yes, Enjoy your ride kiddo.")
            else:
                print(f"Sorry, You paid ${ride_fee_child} which is less than $5")
    elif age <= 18:
        if need_pic == "y":
            ride_fee_teen = int(input("Pay $10\n"))
            if ride_fee_teen >= 10:
                print("Yes, Enjoy your ride WITH PICTURE dude.")
            else:
                print(f"Sorry, You paid ${ride_fee_teen} which is less than $10")
        else:
            ride_fee_teen = int(input("Pay $7\n"))
            if ride_fee_teen >= 7:
                print("Yes, Enjoy your ride dude.")
            else:
                print(f"Sorry, You paid ${ride_fee_teen} which is less than $7")
    else:
        if need_pic == "y":
            ride_fee_adult = int(input("Pay $15\n"))
            if ride_fee_adult >= 15:
                print("Yes, Enjoy your ride WITH PICTURE man.")
            else:
                print(f"Sorry, You paid ${ride_fee_adult} which is less than $15")
        else:
            ride_fee_adult = int(input("Pay $12\n"))
            if ride_fee_adult >= 12:
                print("Yes, Enjoy your ride man.")
            else:
                print(f"Sorry, You paid ${ride_fee_adult} which is less than $12")
else:
    print("Sorry you are too short for the ride.")

