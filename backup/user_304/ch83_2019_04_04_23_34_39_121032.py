def medias_por_inicial(notas):
    inicial={}
    x=0
    contador=0
    c=1
    for nome,valor in notas.items():
        if nome[0] not in inicial:
            x=valor
            inicial[nome[0]]=x
            contador+=1
        else:
            c+=1
            x=x+valor
            m=x/contador
            inicial[nome[0]]=m
    return inicial