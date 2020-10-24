def medias_por_inicial(alunos_notas):
    letra_media = {}
    contador = {}
    for aluno, nota in alunos_notas.items():
        if aluno[0] in letra_media:
            letra_media[aluno[0]] += nota
            contador[aluno[0]] += 1
        else:
            letra_media[aluno[0]] = nota
            contador[aluno[0]] = 1
    for letra, qtd in contador.items():
        letra_media[letra] = letra_media[letra]/qtd

    return letra_media