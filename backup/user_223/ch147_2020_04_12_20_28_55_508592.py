def mais_frequente(l1):
    dic={}
    for e in l1:
        if e in dic:
            dic[e]+=1
        else:
            dic[e]=1
      
    ocorrencias = [0]
    for n in dic.values():
        if n > ocorrencias[0]:
            del ocorrencias[0]
            ocorrencias.append(n)
    for p in dic.keys():
        if dic[p] = ocorrencias
        return p