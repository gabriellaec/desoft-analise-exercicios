def junta_nome_sobrenome(nomes, sobrenomes):
    lista = []
    i = 0
    while i < len(nomes):
        lista.append("{0} {1}".format(nomes[i], sobrenomes[i]))
    return lista
print(lista)