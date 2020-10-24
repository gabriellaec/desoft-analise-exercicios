def eh_crescente(x):

    i = 1
    
    if len(x) == 1 :
        return True
    
    crescente = False
    while i < len(x):
        if x[i] > x[i-1]:
            crescente = True
        else:
            crescente = False
            break 
        i += 1
            

    return crescente