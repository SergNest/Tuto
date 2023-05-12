# riddle        - рядок із зашифрованим словом.
# word_length   – довжина зашифрованого слова.
# start_letter  - літера, з якої починається слово (мається на увазі, що до початку слова літера не зустрічається в рядку).
# reverse       - вказує, у якому порядку записане слово. За замовчуванням — в прямому. Для значення True слово зашифроване 
#                 у зворотньому порядку, наприклад, у рядку 'mi1rewopret' зашифроване слово 'power'.

def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if reverse:
       riddle = riddle[::-1]
    index = riddle.find(start_letter)
    if index != -1:
        some_word = riddle[index: word_length + index]
    return some_word

    
print(solve_riddle('mi1powperet', 3, 'r', True))

# 'mi1powerret'