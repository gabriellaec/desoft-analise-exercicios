def calcula_media(alunos):
    media = 0 
    n = 0
    for dicionario in alunos:
        for keys in dicionario:
            media += dicionario[keys]
            n +=1
    return media/n