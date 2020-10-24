def lista_sufixos(palavra):
    i = 0
    sufixos = []
    while i < len(palavra)-1:
        sufixos += palavra[1:]
    return sufixos     