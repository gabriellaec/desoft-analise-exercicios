def estritamente_crescente (lista):
    
    lista_crescente = []
    ultimo = 0
    
    if len(lista) == 0:
        return lista_crescente
    else:
        for i in lista:
            if i > ultimo:
                ultimo = i
                lista_crescente.append(i)
                
    return lista_crescente                          