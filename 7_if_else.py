#This code added the logical operators

height = int(input("Enter your height in cm: \n"))
bill = 0

if height >= 120:
    print("You are tall enough to ride the rollercoaster!")
    age = int(input("Enter your age: \n"))
    if (age >= 45 and age <= 55):
        bill = 0
        print(f"Midlife crisis tickets are ${bill}.")
    else:
        if age <= 12:
            bill = 5
            print(f"Child tickets are ${bill}.")
        elif age <= 18:
            bill = 7
            print(f"Youth tickets are ${bill}.")
        else:
            bill = 12
            print(f"Adult tickets are ${bill}.")

        need_photo = input("Do you want a photo taken? y or n. \n")
    
        if need_photo == "y":
            bill += 3
            print(f"Your final bill is ${bill}.")
        else:
            print(f"Your final bill is ${bill}.")
else:
    print("You need to grow taller before you can ride.")