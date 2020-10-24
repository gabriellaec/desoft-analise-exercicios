def junta_nome_sobrenome(listan,listas):
    listans = [0]*len(listan)
    for i,e in enumerate(listan):
        listans[i] = '{0} {1}'.format(e,listas[i])