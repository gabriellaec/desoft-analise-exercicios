def lista_sufixos(palavra):
    i = 0
    sufixos = []
    while i <= len(palavra):
        palavra = palavra[i:]
        sufixos.append(palavra)
        i += 1
    return sufixos     