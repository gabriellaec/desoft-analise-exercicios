def mais_populoso(dicioes):
    final={}
    soma=0
    maxi=0
    for i in dicioes.values():
        for e in i:
            soma=soma+e
        if soma>maxi:
            maxi=soma
            es=i
    return es      