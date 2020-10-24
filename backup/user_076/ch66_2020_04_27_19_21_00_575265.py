def lista_sufixos (string):
    lista_sufixos = []
    i = 0
    while i < len(string):
        sufixo = string[i:]
        lista_sufixos.append(sufixo)
    return lista_sufixos
       