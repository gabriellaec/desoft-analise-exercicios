def junta_nome_sobrenome(listan,listas):
    listans = []
    for i,e in enumerate(listan):
        listans.append('{0} {1}'.format(e,listas[i]))
    return listans