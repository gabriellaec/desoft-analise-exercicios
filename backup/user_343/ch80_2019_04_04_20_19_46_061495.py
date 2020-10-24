dic1={'arroz': 1, 'batata': 3, 'coisa': 2}
dic2={'asas': 1,'oiue': 2}

def interseccao_chaves(dic1, dic2):
    lista=[]
    
    for k in dic1.keys():
        lista.append(k)
    for e in dic2.keys():
        if e not in lista: 
             lista.append(e)
    return lista
print (interseccao_chaves(dic1, dic2))    
                       
                       