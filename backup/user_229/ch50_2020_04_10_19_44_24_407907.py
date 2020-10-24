def junta_nome_sobrenome(nomes, sobrenomes):
    lista = []
    i = 0
    while i < len(nomes):
        lista.append("{0} {1}".format(nomes[i], sobrenomes[i]))
        i += 1
    return lista
print(junta_nome_sobrenome(["ana", "maia", "guillermo"], ["teresa", "fleider", "kuznietz"]))