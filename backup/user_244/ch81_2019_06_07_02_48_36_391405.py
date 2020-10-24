def interseccao_valores(x,y):
    
    z = []
    
    
    for v in x.values():
        for i in y.values():
            z.append(v)
            z.append(i)
            
    return z