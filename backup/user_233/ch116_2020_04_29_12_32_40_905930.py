def raiz_quadrada(numero):
    
    contagem = 0
    impar = 1
    
    while numero > 0:
        numero -= impar
        impar += 2
        contagem += 1
    
    if numero == 0:
        return contagem