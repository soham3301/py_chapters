
some_common_errors = [
    "SyntaxError",
    "IndentationError",
    "NameError",
    "TypeError",
    "IndexError",
    "KeyError",
    "AttributeError",
    "ValueError",
    "FileNotFoundError",
]

try:
    file = open("data.txt")
except FileNotFoundError as error:
    file = open("data.txt", mode="w")
    file.write("Something")
else:
    file_content = file.read()
    print(file_content)
finally:
    file.close()

# try:
#     my_dict = {
#         "name": "Soham",
#         "age": 34,
#         "city": "Kamalpur",
#         "hobby": "Coding"
#     }
#     print(my_dict["score"])
# except KeyError as error:
#     print(f"This key doesn't exist: {error}")

# try:
#     number = int(input("Enter a number: "))
# except ValueError as error_message:
#     print(f"{error_message} | This is not a number")