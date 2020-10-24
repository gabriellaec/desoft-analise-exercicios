def calcula_media (alunos):
    soma = 0
    i = 0
    while i < len(alunos):
        dicionario = alunos[i]
        for nota in dicionario.values():
            soma = soma + nota
            media = soma/len(dicinario)
        i = i + 1  
    return media  