def agrupa_por_idade(dic):
    new_dic = {}
    lista_c= []
    lista_ad= []
    lista_ado= []
    lista_i= []
    a = 'criança'
    b = 'adolescente'
    c = 'adulto'
    d = 'idoso'
    for i in dic:
        if dic[i]<=11:
            lista_c.append(i)
            if a not in new_dic:
                new_dic[a] = lista_c
        if dic[i] >= 12 and dic[i] <=17:
            lista_ad.append(i)
            if b not in new_dic:
                new_dic[b] = lista_ad  

                
        if dic[i] >= 18 and dic[i] <= 59:
            lista_ado.append(i)
            if c not in new_dic:
                new_dic[c] = lista_ado
            
        if dic[i] > 60:
            lista_i.append(i)
            if d not in new_dic:
                new_dic[d] = lista_i
                
    return new_dic
                