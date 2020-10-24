
def conta_bigramas(palavra):
    contagem = {}
    i = 0
    while i<len(palavra):
        bi = [''.join(palavra[i:i+2])]
        for e in bi:
            if e in contagem:
                contagem[e]+=1
            else:
                contagem[e]=1
        i+=1
    return contagem