def conta_bigramas(palavra):
    palavra = list(palavra)
    contagem = {}
    i = 0
    while i<(len(palavra)-1):
        bi = [''.join(palavra[i:i+2])]
        for e in bi:
            if e in contagem:
                contagem[e]+=1
            else:
                contagem[e]=1
        i+=1
    return contagem