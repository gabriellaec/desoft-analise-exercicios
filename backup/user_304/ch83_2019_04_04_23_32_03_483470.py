def medias_por_inicial(notas):
    inicial={}
    x=0
    contador=0
    for nome,valor in notas.items():
        if nome[0] not in inicial:
            inicial[nome[0]]=valor
            contador+=1
        else:
            contado+=1
            x=x+valor
            m=x/contador
            inicial[nome[0]]=
    return inicial
