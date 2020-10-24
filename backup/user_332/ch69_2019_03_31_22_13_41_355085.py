def junta_lista (lista):
    lista_t = []
    
    for a in lista:
        if (len(a)>0):
            for i in a:
                lista_t.append(i)
    return lista_t