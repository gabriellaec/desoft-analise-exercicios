def conta_bigramas(palavra):
    return {x+i:palara.count(x+i) for x,i in zip(palavra[:-1], palavra[1:])}