def raiz_quadrada (num):
    subtrair = 1
    i = 0
    while num>1 :
        i += 1
        num -= subtrair
        subtrair += 2
    return i        