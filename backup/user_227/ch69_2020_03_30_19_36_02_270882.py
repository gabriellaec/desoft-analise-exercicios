def junta_listas(lista_composta):
    a = 0
    lista_plana = []
    while a < len(lista_composta):
        b = 0
        
        while b < len(lista_composta[a]):
            lista_plana.append(lista_composta[a][b])
            b += 1
        
        a += 1
    
    return lista_plana