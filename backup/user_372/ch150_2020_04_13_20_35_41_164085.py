def calcula_pi(n):
    soma=0
    i=1
    lista=[]
    while len(lista)<n:
        lista[i-1]=6/(i**2)
        soma+=lista[i]
        i+=1
        pi=(1/2)**soma
        return pi