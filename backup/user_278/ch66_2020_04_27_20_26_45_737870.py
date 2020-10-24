def lista_sufixos(texto):
    l1 = []
    for i in range(0,len(texto)):
        sufixo = [i:]
        l1.append(sufixo)
    return l1