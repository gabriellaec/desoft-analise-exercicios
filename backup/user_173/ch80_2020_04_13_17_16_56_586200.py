def interseccao_chaves (dic1,dic2):
    lista = []    
    for i in range(len(dic1)):
        lista[i] = dic1[dic2[i]]
        
    return lista