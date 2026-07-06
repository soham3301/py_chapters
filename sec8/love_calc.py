def calculate_love_score(name1, name2):
    true_score = 0
    love_score = 0
    true_letters_list = ['t', 'r', 'u', 'e']
    love_letters_list = ['l', 'o', 'v', 'e']
    whole_name = name1 + name2
    for true_match in whole_name:
        if true_match in true_letters_list:
            true_score += 1
    for love_match in whole_name:
        if love_match in love_letters_list:
            love_score += 1
    total_score = str(true_score) + str(love_score)
    print(total_score)
calculate_love_score("angela yu", "jack bauer")
