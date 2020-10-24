def interseccao_valores(dicionario1, dicionario2):
    saida = []
    
    list1 = dicionario1.values()
    list2 = dicionario2.values()
    
    for element in list1:
        if element in list2:
            saida.append(element)
            
    return saida