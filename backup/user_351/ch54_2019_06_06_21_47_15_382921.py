def junta_nome_sobrenome(listan, listas):
    listanova=[]
    for e in listan:
        for i in listas:
            listanova.append(e + " " + i)
    return listanova
        