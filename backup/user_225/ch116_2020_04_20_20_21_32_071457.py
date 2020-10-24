def raiz_quadrada(num):
    x = 1
    i = 0
    while x <= num:
        num-=x
        x+=2
        i+=1
    return i
