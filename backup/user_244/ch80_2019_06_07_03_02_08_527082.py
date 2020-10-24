def interseccao_chaves(x,y):
    z = []
    
    for i in x.keys():
        if i in y.keys():
            z.append(i)
            
    return z