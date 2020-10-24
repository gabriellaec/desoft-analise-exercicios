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
    
def maior_primo_menor_que(n):
    lista=[]
    for i in range(0,n+1):
        if eh_primo(i):
            lista.append(i)
        return lista[-1]
    if n<0:
        return -1
        
            