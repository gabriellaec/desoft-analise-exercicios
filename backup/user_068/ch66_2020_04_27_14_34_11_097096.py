def  lista_sufixos(palavra):
    a = []
    for i in range(len(palavra)):
        t = palavra[i:]
        a.append(t)
    return a