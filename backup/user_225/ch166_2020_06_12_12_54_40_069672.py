def total_semestre_por_bairro(dic):
    e = 0
    novodic = {}
    for i in dic:
        lista = dic[i]
        while e< len(lista):
            gastos = 0
            gastos+=lista[e]
            e+=1
            break
        novodic[i]=gastos
    return novodic