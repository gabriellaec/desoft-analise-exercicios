def calcula_media (alunos):
    soma = 0
    i = 0
    numero = 0
    while i < len(alunos):
        dicionario = alunos[i]
        for nota in dicionario.values():
            numero = numero + 1
            soma = soma + nota
        i = i + 1  
    media = soma/numero
    return media  