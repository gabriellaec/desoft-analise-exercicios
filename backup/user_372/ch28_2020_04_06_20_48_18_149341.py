def soma_numeros(lista):
    soma=0
    i=0
    lista[0]=1
    while i <len(lista):
        lista[i+1]=lista[i]/2
        soma+=lista[i]
        i+=1