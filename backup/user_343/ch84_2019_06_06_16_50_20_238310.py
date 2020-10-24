def inverte_dicionario(n):
    dict={}
    for k,v in n.items():
        if v not in dict:
            dict[v]=[]
       		dict[v].append(k)
    return dict