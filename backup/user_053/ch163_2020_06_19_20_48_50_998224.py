def calcula_media(lista):
    soma_notas = 0
    total_alunos = 0
    for dic in lista:
        for nota in dic.values():
            soma_notas += nota
            total_alunos += 1
    return soma_notas/total_alunos