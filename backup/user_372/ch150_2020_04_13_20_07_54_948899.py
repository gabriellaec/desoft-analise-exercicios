def calcula_pi(n):
    soma=0
    i=0
    lista=[]
    n=len(lista)
    while i<n:
        lista[i]=6/(i**2)
        soma+=lista[i]
        soma==(1/2)**soma
        i+=1
        return soma