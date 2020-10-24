def interseccao_chaves(dicionario1,dicionario2):
    lista=[]
    for i in dicionario1.keys():
        for e in dicionario2.keys():
            if i==e:
                lista.append(i)
        
  
        
    return lista
