def interseccao_valores(dict1, dict2):
    lista=[]
    
    for a in dict1.values() :
        for b in dict2.values():
            if a==b:
                lista.append(a)
    return lista