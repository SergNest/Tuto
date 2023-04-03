num = int(input("Enter integer (0 for output): "))
sum = 0

while True:
    if num == 0:
        break
    for i in range(num):
        sum += i

    print(sum)    
    num = int(input("Enter integer (0 for output): "))
    