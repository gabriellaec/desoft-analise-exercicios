def quantos_uns(numero):
    i = 0
    contador = 0
    while i < len(numero):
        if numero[i] == 1:
            contador += 1
            posicao = i
        else: 
            i += 1
    return posicao
        
        