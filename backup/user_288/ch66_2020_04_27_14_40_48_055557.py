def lista_sufixos(palavra):
    i = 1
    sufixos = []
    while i < len(palavra)-1:
        palavra = palavra[i:]
        sufixos.append(palavra)
        i += 1
    return sufixos     