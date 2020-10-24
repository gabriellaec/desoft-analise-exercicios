def conta_bigramas(palavra):
    print(palavra[:-1],palabra[1:])
    
    return {x+i:palavra.count(x+i) for x,i in zip(palavra[:-1], palavra[1:])}