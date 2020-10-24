def lista_sufixos(texto):
    l1 = []
    for i in range(0,len(texto)):
        sufixo = texto[i:]
        l1.append(sufixo)
    return l1