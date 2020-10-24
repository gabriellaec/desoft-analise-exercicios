def faixa_notas(lista):
    i= 0
    cont1 =0
    cont2 = 0
    cont3 = 0
    lista_nova = []
    lista= [3, 2,3,3,3,3,3,3,3,3,9,9,9,5]
    while i<len(lista):
        if lista[i]>= 0 and lista[i] <5:
            cont1+=1
            
        elif lista[i]>=5  and lista[i]<=7:
            cont2+=1
        
        elif lista[i]>7  and lista[i]<=10:
            cont3+=1
        
        i+=1

    lista_nova.append(cont1)
    lista_nova.append(cont2)
    lista_nova.append(cont3)
    return lista_nova



