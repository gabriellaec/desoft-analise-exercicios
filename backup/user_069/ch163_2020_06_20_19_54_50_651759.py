def calcula_media(alunos):

    s = 0
    c = 0

    for dicionario in alunos:

        for nota in dicionario.values():
            s += nota
            c += 1

    media = s/c

    return media