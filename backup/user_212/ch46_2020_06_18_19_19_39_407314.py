def numero_no_indice(lista):
    lista_iguais=[]
    
    indice = 0
    for e in lista:
        if e == indice:
            lista_iguais.append(e)
        indice +=1
        
    return lista_iguais