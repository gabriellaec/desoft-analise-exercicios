def total_do_semestre_por_bairro(dic):
    e = 0
    novodic = {}
    for i in dic:
        lista = dic[i]
        gastos = 0
        e = 0
        while e< len(lista):
            gastos+=lista[e]
            e+=1
        novodic[i]=gastos
    return novodic