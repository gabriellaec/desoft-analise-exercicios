def mais_populoso(dic):
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
                Maiorest=ks[j]           
        Total=0
    return Maiorest