def calcula_media (alunos):
    i = 0
    lista_notas = []
    while i < len(alunos):
        for nota in alunos[i].values():
            lista_notas.append(nota)
        i += 1
    media = sum(lista_notas) / len(lista_notas)
    return media