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
            if numero == 0:
                conta = False
                raiz = raiz + 1
        impares = impares + 2
    return raiz
        
        
        