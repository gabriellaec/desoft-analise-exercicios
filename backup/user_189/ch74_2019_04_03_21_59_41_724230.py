def conta_bigramas(palavras):
    contagem={}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra]+=1
        else:
            contagem[palavra]=1
    return contagem
print(conta_palavras(lista))