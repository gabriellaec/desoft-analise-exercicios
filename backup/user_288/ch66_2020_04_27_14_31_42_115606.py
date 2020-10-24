def lista_sufixos(palavra):
    i = 0
    sufixos = []
    while i < len(palavra)-1:
        palavra2 = palavra[i][1:]
        sufixos.append(palavra2)
        i += 1
    return sufixos     