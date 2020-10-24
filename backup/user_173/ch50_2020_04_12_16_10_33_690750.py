def junta_nome_sobrenome (lista1,lista2):
    lista3 = []
    i = 0
    while i < len(lista1) and i<len(lista2):
        lista3.append(lista1[i] + ' ' + lista2[i])
        i += 1
    
    return lista3                 
                  