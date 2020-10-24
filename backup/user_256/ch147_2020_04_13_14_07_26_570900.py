def mais_frequente(palavras):
    contagem = {}
    for elementos in palavras:
        if not elementos in contagem:
            contagem[elementos] = 1
        else:
            contagem[elementos]+=1
    maxima=0
    for palavra in contagem:
        if contagem[palavra]> maxima:
            maxima = contagem[palavra]
            palavra_mais_freq=palavra
    return palavra_mais_freq
        