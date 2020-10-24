def interseccao_valores(dic1,dic2):
    l=[]
    l1=[]
    for nomes,valores in dic1.items():
        l1.append(valores)
    for nomes,valores in dic2.items():
        if valores in l1:
            l.append(valores)
    return l
