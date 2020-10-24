def monta_mala(lista):
    lista_final=[]
    i=0
    peso=0
    while peso<23:
        peso+=lista[i]
        if peso<=23:
            lista_final.append(lista[i])
            i+=1
    return lista_final
    
    
         