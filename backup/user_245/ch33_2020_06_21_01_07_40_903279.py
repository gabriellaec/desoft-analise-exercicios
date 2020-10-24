def primos_entre(a,b):
    num = 0
    impar = 3
    #check if n = primo
    for i in range(a,b+1):
        if i % 2 == 0:
            if i!=2:
                num += 0
            else:
                num += 1
        elif i ==1:
            num += 0
        else:
            while impar<i:
                if i%impar == 0:
                    num += 1
    return num
            