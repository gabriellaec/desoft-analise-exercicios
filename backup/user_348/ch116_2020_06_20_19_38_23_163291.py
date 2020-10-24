def raiz_quadrada (n):
    impares = 3
    raiz = 0
    numero = n - 1
    if n == 0:
        raiz = 0
        return raiz
    elif n == 1:
        raiz = 1
        return raiz
    conta = True
    while conta:
        numero = numero - impares
        if impares >= numero:
            conta = False
        raiz += 1
        impares = impares + 2
    return raiz     
        
        