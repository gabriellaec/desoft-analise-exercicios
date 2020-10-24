def calcula_pi(n):
    lista=[]
    for n in range(0, n):
        lista.append(6/n**2)
    soma=sum(lista)
    return soma**1/2
    