def lista_caracteres (palavra):
    l=[]
    for e in palavra:
        if e not in l: 
            l.append(e)
    return l