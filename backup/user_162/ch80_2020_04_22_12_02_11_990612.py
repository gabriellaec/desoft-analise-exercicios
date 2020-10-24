
def interseccao_chaves(lis_dic):
    lista = []
    for dic1 in lis_dic[0]:
        for cahves in dic1:
            lista.append(dic1)
            
    for dic2 in lis_dic[1]:
        for cahves in dic2:
            lista.append(dic2)
            
    return lista
