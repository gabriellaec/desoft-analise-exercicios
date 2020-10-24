def acha_bigramas(string):
    n=2
    x=[string[i:i+n] for i in range(0, len(string), n)]
    return x