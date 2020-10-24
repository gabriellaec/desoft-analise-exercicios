def soma_impares(soma):
    lista=[]
    listai=lista
    i=0
    soma=0
    for i in range (1,len(lista),2):
        if listai[i]%2==0:
            del listai[i]
            i+=1
            soma+=listai
    return soma