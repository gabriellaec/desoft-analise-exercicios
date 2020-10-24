def simplifica_dict(x):
    lista = []
    lista_certa = []
    for e,k in x.items():
        if e in lista:
            lista.append(0)
        else:
            lista.append(e)
        if k in  lista:
            lista.append(0)
        else:
            lista.append(k)
    for zero in lista:
        if zero == 0:
            del zero
        else:
            lista_certa.append(zero)
    return lista_certa