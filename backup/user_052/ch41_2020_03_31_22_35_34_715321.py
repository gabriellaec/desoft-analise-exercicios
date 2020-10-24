def zera_negativos(num):
    i = 0
    while i < len(num):
        if num[i] < 0:
            num[i] = 0
        else:
            i+=1
        return num
            
    