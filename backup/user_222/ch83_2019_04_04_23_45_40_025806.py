def medias_por_inicial(dicionario):
    dicionario_resultado={}
    media=0
    contagem=0
    valor_adicionado=0
    valor_t=0
    for k,v in dicionario.items():
        if k[0] not in dicionario_resultado:
            contagem+=1
            valor_t=v
            dicionario_resultado[k[0]]=v
        else:
            valor_adicionado=v
            media=(valor_adicionado+valor_t+v)/(contagem+1)
            dicionario_resultado[k[0]]=media
    return dicionario_resultado