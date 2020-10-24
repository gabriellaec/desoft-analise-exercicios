def raiz_quadrada (n):
    impares = 3
    raiz = 0
    conta = True
    while conta:
        if raiz == 0:
            numero = n - 1
        else:
            numero = numero - impares
            if numero == 0:
                conta = False
        impares = impares + 2
        raiz = raiz + 1
    return raiz
        
        
        