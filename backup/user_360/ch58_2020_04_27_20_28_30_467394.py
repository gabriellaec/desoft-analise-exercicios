def conta_a(texto):
    cont = 0
    i = 0
    x = len(texto)
    while i < x:
        if texto[i] == 'a':
            cont+=1
            i+=1
        else:
            i+=1
    return cont
    
  