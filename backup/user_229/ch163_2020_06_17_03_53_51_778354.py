def calcula_media(lista_dicionarios):
    total = 0
    quantos_alunos = 0
    for dicionario in lista_dicionarios:
        for aluno in dicionario:
            total += dicionario[aluno]
            quantos_alunos += 1
    media = total/quantos_alunos
    return media