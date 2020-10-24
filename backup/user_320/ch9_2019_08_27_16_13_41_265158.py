def lista_sufixos(string):
    sufixos = []
    cont = 1
    rascunho = []
    while cont < len(string):
        for letra in string[cont:]:
            rascunho.append(letra)
        sufixos.append(rascunho.copy())
        rascunho.clear()
        cont += 1

    return sufixos