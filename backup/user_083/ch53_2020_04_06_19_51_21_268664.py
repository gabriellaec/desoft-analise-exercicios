def soma_impares(soma):
    lista=[]
    listai=lista
    soma=0
    i=0
    for c in range (1,len(lista),2):
        if listai[i]%2==0:
            del listai[i]
            i+=1
            soma+=listai
    return soma