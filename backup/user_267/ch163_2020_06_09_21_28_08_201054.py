def calcula_media(lista):
    soma = 0
    alunos = 0
    c = 0
    while c < len(lista):
        dicio = lista[c]
        for gr in dicio.values():
            soma += gr
            alunos += 1
        c += 1
    media = soma/alunos
    return media
            
            