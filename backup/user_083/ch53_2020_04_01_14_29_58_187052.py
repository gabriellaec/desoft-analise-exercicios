def soma_impares(x):
    lista=[]
    listai=lista
    i=0
    soma=0
    while i<=len(lista):
        if listai[i]%2==0:
            del listai[i]
            i+=1
            soma+=listai
    return soma