def lista_caracteres(st):
    carac = []
    for i in st:
        if i not in carac:
            carac.append(i)    
    
    return carac