def conta_letras(palavra):
    contagem={}
    for letras in palavra:
        if not letras in contagem:
            contagem[letras]=1
        else:
            contagem[letras]+=1
    return contagem