def eh_crescente(lista):
    i = 1
    resposta = True
    while i < len(lista):
        if lista[i] <= lista[i-1]:
            resposta = False
        i += 1
    return resposta
            
        