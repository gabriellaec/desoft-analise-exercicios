def  calcula_total_da_nota(lista1,lista2):
    lista=[]
    i=0

    while i < len(lista1):
        lista.append(lista1[i]*lista2[i])
        i+=1
    soma=0
    x=0
    while x<len(lista):
        soma+=lista[x] 
        x+=1
    return soma
