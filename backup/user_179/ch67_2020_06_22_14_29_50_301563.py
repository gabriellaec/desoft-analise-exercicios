def alunos_impares (alunos):
    lista = []
    for i in range(len(alunos)):
        if i % 2 != 0:
            lista.append(alunos[i])
    return lista