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
def primos_entre(a,b):
    lista=[]
    for i in range(a,b+1):
        if eh_primo(i)==True and eh_primo(i)>0:
            lista.append(i)
    return (lista)