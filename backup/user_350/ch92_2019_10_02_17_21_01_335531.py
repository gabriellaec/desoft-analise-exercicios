def simplifica_dict(dicionario):
    lista_sem_repetir = []
    for e in dicionario:
        if e not in lista_sem_repetir:
            lista_sem_repetir.append(e)
    for i in  dicionario.values():
        if i not in lista_sem_repetir:
            lista_sem_repetir.append(i)
    return lista_sem_repetir