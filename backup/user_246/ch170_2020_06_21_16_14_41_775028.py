def apaga_repetidos(p):
    p = list(p)
    i=0
    while i < len(p):
        if i != p.index(p[i]):
            p[i] = '*'
        i += 1
    p = str(p)
    x = p.replace(',',' ')
    x = x.replace("'",' ')    
    x = x.replace('[', '')    
    x = x.replace(']', '')    
    x = x.replace(' ', '-')   
    x = x.replace('--', '')   
    x = x.replace('-', ' ')  
    x = x.strip()    
    return (x)
        