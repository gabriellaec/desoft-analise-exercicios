def eh_primo(numero):
    inicio = 1
    contar_divisores = 0
    while inicio<=numero:
        if numero%inicio==0:
            contar_divisores +=1
        inicio = inicio + 1
    if contar_divisores > 2:
        return False
    elif (numero==0 or numero==1):
        return False
    else:
        return True

def verifica_primos(lista):
    dic = {}
    for i in range(len(lista)):
        if eh_primo(lista[i]):
            dic[lista[i]]=True
        else:
            dic[lista[i]]=False
    return dic
        
        

    