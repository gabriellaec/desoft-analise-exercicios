def conta_bigramas(texto):
    contagem = {}
    i=0
    while i < len(texto) - 1:
        if not (texto[i]+texto[i+1]) in contagem:
            contagem[texto[i]+texto[i+1]]  = 1
        else:
            contagem[texto[i]+texto[i+1]] += 1
        i+=1
    return contagem