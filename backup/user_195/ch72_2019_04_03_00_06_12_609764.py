def lista_caracteres(s):
    i=0
    L=[]
    while i<len(s):
        if s[i] in L:
            L.append(s[i])
        i+=1
    return L