import random
words = ['ant', 'bat', 'camel', 'cat', 'crow', 'deer', 'dog', 'eagle', 'ferret', 'goose', 'hawk', 'llama', 'moose', 'mouse', 'otter', 'owl', 'parrot', 'rabbit', 'raven', 'seal', 'sloth', 'tiger', 'turtle', 'wolf', 'zebra']
user_lives = 0

# Generating Random Word & Similar Length Blank
def generate_randoms():
    random_word = random.choice(words)
    random_blanks = "_"
    for _ in range(0, len(random_word) - 1):
        random_blanks += "_"
    return [random_word, random_blanks]

randoms = generate_randoms()
secret_word = randoms[0]
dashes = randoms[1]
print(f"Here is the secret word: {secret_word}")
print(f"Here are the dashes: {dashes}, {type(dashes)}, {len(dashes)}")

while dashes.count("_") > 0:
    # Asking the user to guess a letter
    def user_guess():
        global dashes
        user_reply = str(input(f"""                                              
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/
    Word to guess: {dashes}
    Guess a letter: """))
        return user_reply


    # Checking if the user input matches a letter inside the random word and updating the dashes
    user_guess = user_guess()

    if user_guess in secret_word:
        print("It's available")
        all_indexes = [idx for idx, val in enumerate(secret_word) if val == user_guess]
        print(f"Index / Indexes of the matched character: {all_indexes}")
        if user_guess not in dashes:                                                                #   <--- this will not work if there are 3 or more similar chars inside the secret word
            updated_dashes = dashes[:all_indexes[0]] + user_guess + dashes[all_indexes[0] + 1 :]
        else:
            updated_dashes = dashes[:all_indexes[1]] + user_guess + dashes[all_indexes[1] + 1 :]
        dashes = updated_dashes
        print(f"Updated dashes with user input: {dashes}")
    else:
        print("NO MATCH FOUND")
