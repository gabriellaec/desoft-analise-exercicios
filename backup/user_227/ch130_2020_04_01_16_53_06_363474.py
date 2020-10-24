def monta_mala(pesos_de_itens):
    lista_final=[]
    total=0
    i=0
    while i<len(pesos_de_itens):
        total+=pesos_de_itens[i]
        
        if total<=23:
            lista_final.append(pesos_de_itens[i])
        
        i+=1
    
    return(lista_final)