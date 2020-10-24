def lista_sufixos(palavra):
    i = 0
    sufixos = []
    while i < len(palavra):
        sufixos += palavra[1:]
    return sufixos     