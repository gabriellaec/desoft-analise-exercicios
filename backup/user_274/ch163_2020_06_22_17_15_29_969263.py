def calcula_media(alunos):
    a = 0
    b = 0
    for i in alunos:
        for j in i.values():
            a = a + j
            b = b + 1
    return a/b