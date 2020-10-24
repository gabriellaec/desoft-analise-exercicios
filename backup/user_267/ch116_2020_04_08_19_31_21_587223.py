def raiz_quadrada(num):
    i = 1
    conta= 0
    while num > 0:
        num -= i
        i += 2
        conta +=1      
    return conta
        