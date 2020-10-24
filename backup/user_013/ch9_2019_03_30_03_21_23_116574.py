def lista_sufixos(P):
    A = []
    i = 0
    if len(P) == 0 or len(P)==1:
        A.append(P[0]) 
        return A
    while i <= len(P):
        A.append(P[i:len(P)+1])
        i += 1
    return A            
