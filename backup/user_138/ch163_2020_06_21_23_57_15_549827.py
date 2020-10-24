def calcula_media (lista):
    i = 0
    soma = 0
    for turma in lista:
        for nota in turma.values():
            soma += nota
            i+=1
    media = soma/i
    return media