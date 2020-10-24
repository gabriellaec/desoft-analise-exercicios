def calcula_media(alunos):
    notas = []
    for dic in alunos:
        for nota in dic.values():
            notas.append(nota)
    return sum(notas)/len(notas)