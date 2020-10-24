def lista_sufixos(palavra):
    i = 0
    sufixos = []
    while i < len(palavra)-1:
        palavra[i] = palavra[1:]
        sufixos.append(palavra[i])
        i += 1
    return sufixos     