def lista_caracteres(s):
    l=[]
    
    for i in s:
        if i not in l:
            l.append(i)
    
    return l