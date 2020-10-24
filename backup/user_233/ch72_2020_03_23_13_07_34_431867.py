def lista_caracteres(string):
    
    caracteres = []
    
    for c in string:
        if c in caracteres: continue
        caracteres.append(c)
    
    return caracteres