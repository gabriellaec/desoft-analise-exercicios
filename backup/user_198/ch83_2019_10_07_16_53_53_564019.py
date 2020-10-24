def medias_por_inicial(nomes):
    media={}
    cont_letra={}
    for aluno in nomes:
        if not aluno[0] in cont_letra:
            cont_letra[aluno[0]]=1
        else:
            cont_letra[aluno[0]]+=1
        if not aluno[0] in media:
            media[aluno[0]]=nomes[aluno]
        else: 
            media[aluno[0]]+=nomes[aluno]
    for aluno in media:
        media[aluno[0]]/=cont_letra[aluno[0]]
    return media