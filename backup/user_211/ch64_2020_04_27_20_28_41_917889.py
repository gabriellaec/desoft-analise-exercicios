def acha_bigramas(string):
    return list({x+y:None for x,y in zip(string[:-1],string[1:])})
