n = int(input("numero inicial: "))
num = n
while num != 1:
    if num == 2:
        num = num/2   
    elif num % 2 == 0:
        num = num/2
    elif num % 2 != 0:
        num = 3*num + 1