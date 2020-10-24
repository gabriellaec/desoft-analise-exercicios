def calcula_total_da_nota (lista1,lista2):
    
    i=0
    lista_valor=[]
    
    while(i<len(lista1)):
        
        lista_valor.append(float(lista1[i])*float(lista2[i]))
        i+=1
    
    j=0
    preco=0

    while(j<len(lista_valor)):
        preco+=lista_valor[j]
        j+=1
    
    return preco