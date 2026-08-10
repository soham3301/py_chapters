
numbers = [3, 1, 66, 24, 31, 73, 21, 9]
added_10_numbers = [item - 100 for item in numbers]
print(added_10_numbers)

name = "Soham"
letters_list = [letter for letter in name]
print(letters_list)

range_output_list = [number * 2 for number in range(1, 5)]
print(range_output_list)

#? List Comprehension with condition

names = ["Raj", "Bubai", "Rony", "Payel", "Tanu", "Akash", "Uttam", "Mallika"]
names_with_4_letters = [the_name for the_name in names if len(the_name) <= 4]
print(names_with_4_letters)

names_uppercase = [u_name.upper() for u_name in names if len(u_name) > 4]
print(names_uppercase)

3
6
13
5
7
89
12
3
33
34
1
344
42
