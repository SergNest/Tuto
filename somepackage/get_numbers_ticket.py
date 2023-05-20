from random import randrange


def get_numbers_ticket(min, max, quantity):    
    list = []
    if min > quantity > max or min < 1 or max > 1000:
        return list 
    while len(list) < quantity:
        intr = randrange(min, max+1)
        if intr not in list:
            list.append(intr)
    l = sorted(list)        
    return l


print(get_numbers_ticket(1, 50, 5))