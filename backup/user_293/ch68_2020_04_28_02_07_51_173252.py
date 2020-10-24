def separa_trios(lista_alunos):
    lista_trio = []
    i = 0
    a = 3
    for e in lista_alunos:
        b = lista_alunos[i:a]
        lista_trio.append(b)
        return lista_trio
        i += 3
        a += 3