def conta_letras(a):

    
    entrega = {}

    for i in a:
        if i not in entrega:
            entrega[i] = 1
        
        else:
            entrega[i] += 1

    return(entrega)