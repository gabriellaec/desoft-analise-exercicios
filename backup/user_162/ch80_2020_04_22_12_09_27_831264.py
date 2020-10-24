def interseccao_chaves(lis_dic):
    lista1 = []
    lista2 = []
    lista = []
    
    for dic1 in lis_dic[0]:
        for cahves in dic1:
            lista1.append(dic1)
            
    for dic2 in lis_dic[1]:
        for cahves in dic2:
            lista2.append(dic2)
        for i in lista1:
            if i == lista2[-1]:
                lista.append(i)
    
    return lista