def conta_bigramas(palavra):
    return {x+i:palavra.count(x+i) for x,i in zip(palavra[:-1], palavra[1:])}