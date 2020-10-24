def alunos_impares(nomes):
    lista = []
    if len(nomes) == 1:
        pass
    else:
        for i in range(0,len(alunos)):
            if i%2 != 0:
                lista.append(nomes[i])
    return lista
                         