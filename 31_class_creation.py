class Car:
    def __init__ (self, seats):
        self.seats = seats

my_car = Car(3)

print(my_car.seats)

class Student:
    def __init__(self, name, marks, age):
        self.name = name
        self.marks = marks
        self.age = age
        self.good_or_bad = True

        if marks < 50:
            self.good_or_bad = False

raaj = Student("Raaj", 90, 15)
rohit = Student("Rohit", 44, 15)

print(raaj.good_or_bad)
print(rohit.good_or_bad)

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, another_user):
        another_user.followers += 1
        self.following += 1

soham = User("001", "Soham")
amitabh = User("002", "Amitabh")

soham.follow(amitabh)

print(f"Amitabh Followers: {amitabh.followers} and his Following: {amitabh.following}")
print(f"Soham Followers: {soham.followers} and his Following: {soham.following}")
        