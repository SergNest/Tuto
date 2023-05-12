def token_parser(s):
    list_check = ["*", "/", "-", "+", '(',')']
    list_return = []
    next =''
    for letter in s:
        if letter.isdigit():
            next += letter
        elif letter in list_check:
            if next:
                list_return.append(next)
            next = ''
            list_return.append(letter)
        elif letter.isspace() and next:
            list_return.append(next)
            next = '' 
    if next:
        list_return.append(next)        
    return list_return


print(token_parser("2+ 34-5 * 3"))
