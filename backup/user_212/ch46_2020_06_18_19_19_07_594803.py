def numero_no_indice(lista):
    lista_iguais=[]
    
    indice = 0
    for e in lista:
        if e == indice:
            e.append(lista_iguais)
        indice +=1
        
    return lista_iguais