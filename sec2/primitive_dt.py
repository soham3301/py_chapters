#This is the lecture on primitive data types
#Chapter 2

print("Hello"[4])
print("Hello"[-1])

print(len("Hello"))


print(type("123"))
print(type(123))
print(type(123.123))
print(type(True))

print("Number of letters in your name: ", len(input("Enter your name")))

print("My age " + str(34))
print(34 + 10)
print(34 - 5)
print(5 * 3)
print(100 / 20)

print(100 // 20)
print(5 / 3)
print(5 // 3)

print(2 ** 3)

print("=== FSTRING ===")

top_score = 75
name = "Soham"
is_winning = False
your_point = 22.25

print(f"Your name is {name} and your point is {your_point}. Here the top score is {top_score}")
