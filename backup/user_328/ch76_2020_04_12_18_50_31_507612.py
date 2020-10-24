def aniversariantes_de_setembro(lista):
    dict = {}
    i=0
    nomedata = lista.values()
    for k,v in lista.items():
        if v[3] == '0' and v[4] == '9':
            dict[k] = v
            i += 1
    return dict
        