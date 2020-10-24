def agrupa_por_idade(string):
    i = 0 
    nome= []
    entrada= {}
    saida= {}
    for k, v in string.items():
        nome.append(k)
        if v not in saida:
            amanda = [k]
            saida[v]= amanda
        elif v in saida:
            amanda = [k]
            saida[v] += amanda
    return saida
