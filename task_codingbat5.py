"""
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
We are in trouble if the parrot is talking and the hour is before 7 or after 20.
Return True if we are in trouble.

"""
def parrot_trouble(talking, hour):
    if (talking and hour < 7) or (talking and hour > 23):
        return True
    else:
        return False

print(parrot_trouble(True, 21)) # True
print(parrot_trouble(True, 7)) # False
print(parrot_trouble(False, 6)) # False


# def split_list(grade):
#     k1 = []
#     k2 = []
#     if grade:
#         sumloc = sum(grade) / len(grade)
#         for i in grade:
#             if i <= sumloc:
#                 k1.append(i)
#             else:
#               k2.append(i)
    
#     return k1, k2

# print(split_list([1,5,6,7,8,9,10]))