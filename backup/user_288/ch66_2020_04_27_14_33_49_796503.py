def lista_sufixos(palavra):
    i = 0
    sufixos = []
    while i < len(palavra):
        palavra[i] += palavra[1:]
        sufixos.append(palavra[i])
        i += 1
    return sufixos     