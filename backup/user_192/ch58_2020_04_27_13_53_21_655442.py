def conta_a(texto):
    a=0
    i=0
    while i < len(texto):
        if texto[i] == 'a':
            a+=1
        i+=1   
    return a    