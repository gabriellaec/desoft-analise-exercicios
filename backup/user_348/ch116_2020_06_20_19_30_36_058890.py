def raiz_quadrada (n):
    impares = 3
    raiz = 0
    conta = True
    while conta:
        if raiz == 0:
            numero = n - 1
            raiz += 1
        else:
            numero = numero - impares
            raiz = raiz + 1
            if impares >= numero:
                conta = False
        impares = impares + 2
    return raiz
        
        
        