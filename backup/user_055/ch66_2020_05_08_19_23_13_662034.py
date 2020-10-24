def lista_sufixos(string):
    sufixos = []
    l = 0
    while l < len(string):
        sufixos.append(string[l::])
        l += 1
    return sufixos