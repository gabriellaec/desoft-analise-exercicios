def conta_bigramas(palavra):
    print(palavra[:-1])
    print(palavra[1:])
    
    return {x+i:palara.count(x+i) for x,i in zip(palavra[:-1], palavra[1:])}