def mais_frequente(l1):
    dic={}
    for e in l1:
        if e in dic:
            dic[e]+=1
        else:
            dic[e]=1
           
    for n in dic.values():
        ocorrencias = [0]
        if n>ocorrencias[0]:
            ocorrencias.clear()
            ocorrencias.append(n)
            
    ocorrencias_p = ocorrencias[0]
    
    for p,o in dic.items():
        if o == ocorrencias_p:
            return p