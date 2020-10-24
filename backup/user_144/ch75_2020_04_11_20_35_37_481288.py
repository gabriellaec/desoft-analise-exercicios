    
def verifica_primos(lista):
    dic = {}
    contador = 0
    for i in range(1, lista[i] + 1):
        if lista[i] % i == 0:
            contador += 1
    if contador == 2:
        dic[i] = True
    else:
        dic[i] = False
        
    return dic