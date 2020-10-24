def lista_sufixos(palavra):
    i = 0
    sufixos = []
    while i < len(palavra):
        palavra2 = palavra[1:]
        sufixos.append(palavra2)
        i += 1
    return sufixos     