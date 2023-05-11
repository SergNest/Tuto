def capital_text(s):
    listsymbls = ['.', '!', '?']
    new_string = ''

    f_enter = True
    dotittel = False
    for el in s.split(" "):
        
        if f_enter:
            f_enter = False 
            new_string += el.title() +' '
            dotittel = el[-1] in listsymbls
            continue

        if el.isalpha() and el[-1] in listsymbls:
            dotittel = True
        elif dotittel:
           new_string += el.title() + ' '
           dotittel = el[-1] in listsymbls
        else:
            new_string += el+ ' '
            dotittel = el[-1] in listsymbls
            
    return new_string.split()


print(capital_text('hello world! awesome? yes'))
