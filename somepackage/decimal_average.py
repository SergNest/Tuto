from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    aver = 0
    for nun in number_list:
        aver += Decimal(nun)
    
    return Decimal(aver / Decimal(len(number_list)))
    
    
        
print(decimal_average([3, 5, 77, 23, 0.57], 6))
print(decimal_average([31, 55, 177, 2300, 1.57], 9))