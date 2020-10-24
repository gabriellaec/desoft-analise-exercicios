def conta_letras(palavra):
    contagem={}
    for letras in palavra:
        if not letras in contagem:
            contagem[palavra]=1
        else:
            contagem[palavra]+=1
    return contagem
