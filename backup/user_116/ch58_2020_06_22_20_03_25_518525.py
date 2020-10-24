def conta_a(x):
    x=str(x)
    i=0
    contador_de_a=0
    while i<len(x):
        if x[i]==("a"):
            contador_de_a+=1
            i+=1
        else:
            i+=1
    return contador_de_a