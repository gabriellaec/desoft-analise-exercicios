def total_do_semestre_por_bairro(dic):
    e = 0
    novodic = {}
    for i in dic:
        lista = dic[i]
        gastos = 0
        e = 0
        novalista = []
        while e<len(lista):
            k = lista[-e]
            novalista.append(k)
            if e == 6:
                break
            e+=1
        e = 0
        while e<len(novalista):
            gastos+=novalista[e]
            e+=1
        novodic[i]=gastos
    return novodic