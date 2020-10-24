def raiz_quadrada(num):
    contador = 0
    impar = 1
    while num > 0:
        num -= impar
        impar += 2
        contador += 1
    return contador

    
        