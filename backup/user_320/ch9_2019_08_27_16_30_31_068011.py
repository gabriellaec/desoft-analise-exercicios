def lista_sufixos(string):
    string = string.replace(' ', '')
    sufixos = []
    cont = 1
    rascunho = []
    while cont < len(string):
        for letra in string[:]:
            rascunho.append(letra)
        sufixos.append(''.join(rascunho[::-1]))
        rascunho.clear()
        cont += 1

    return sufixos[::-1]