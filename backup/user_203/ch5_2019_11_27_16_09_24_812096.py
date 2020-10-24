[13:04, 27/11/2019] Rubito: def eh_primo (x):
    if x==2:
        return True
    elif x==1 or x==0:
        return False
    elif x%2==0:
        return False
    else:
        n = 3
        while n < x:
            if x%n==0:
                return False
            n=n+2
        else: 
            return True
def maior_primo_menor_que(j):
    lista = []
    for z in range(j+1):
        if eh_primo(z)==True:
            lista.append(z)
    if len(lista)==0:
        return -1
    else:
        return lista[-1]
[13:05, 27/11/2019] Desa: def eh_crescente(lista):
    posicao=1
    contador=1
    if len(lista)==0:
        return True
    maior=lista[0]
    while posicao<len(lista):
        if lista[posicao]>maior:
            maior=lista[posicao]
            contador+=1
        posicao+=1
    if len(lista)==contador:
        return True
    else:
        return False