def lista_sufixos(txt):
    a = []
    for i in range(len(txt)):
        sufixo = txt[i:]
        a.append(sufixo)
    return a