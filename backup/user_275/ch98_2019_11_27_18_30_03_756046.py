def bairro_mais_custoso(dic):
    Total=0
    Maior=0
    for k in dic:
        ks=list(dic)
    for k in dic.values():
        Valores=k
    for j in range(len(Valores)-1):
        for i in Valores.values():
            Total+=i
            if Total > Maior:
                MaiorB=ks[j]           
        Total=0
    return MaiorB