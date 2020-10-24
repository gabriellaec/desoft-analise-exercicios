def lista_sufixos (string):
    i = 0
    sufixos = []
    while i < (len(string)) :
        percorre = string[i:]
        sufixos.append(percorre)
        i += 1
    return sufixos