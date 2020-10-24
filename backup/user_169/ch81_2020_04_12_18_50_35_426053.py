def interseccao_chaves(dicionario1,dicionario2):
    lista=[]
    for i in dicionario1.values():
        for e in dicionario2.values():
            if i==e:
                lista.append(i)
        
  
        
    return lista