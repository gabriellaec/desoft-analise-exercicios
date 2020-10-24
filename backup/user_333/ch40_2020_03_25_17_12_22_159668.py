def soma_valores(lista):
    soma=0
    n=int(len(lista))-1
    while n>=0:
        soma=soma+lista[n]
        n-=1
    return soma