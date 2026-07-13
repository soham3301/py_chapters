user_input = int(input("Enter Number: "))

def is_prime(num):
    numbers_list = []
    for numbers in range(num):
        numbers_list.append(numbers)
    numbers_list.pop(0)
    numbers_list.pop(0)
    print(numbers_list)
    for number in numbers_list:
        if num % number == 0:
            print("Not Prime")
            return False
    print("Prime")
    return True


is_prime(user_input)
