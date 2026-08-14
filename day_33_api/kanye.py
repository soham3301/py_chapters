
import requests

while True:
    user_choice = input('''
Enter 1 for next quote
Enter 0 for exit
''')
    if user_choice == "0":
        break
    elif user_choice == "1":
        response = requests.get("https://api.kanye.rest/")
        quote = response.json()["quote"]
        print(quote)
    else:
        continue
