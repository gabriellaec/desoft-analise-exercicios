def conta_ocorrencias(lista):
    contagem={}
    for palavra in lista:
        if not palavra in contagem:
            contagem[palavra]=1
        else:
            contagem[palavra]+=1
    return contagem
            