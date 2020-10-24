def  calcula_total_da_nota(lista1,lista2):
    i=0
    lista=[]
    
    while i<len(lista1):
        lista.append('{0}'.format(lista1[i]*lista2[i]))
        i+=1
    soma=0
    p=0
    while p<len(lista):
        soma+=lista[p]
        p+=1
    return soma