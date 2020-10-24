def lista_sufixos(palavra):
    i = 1
    sufixo = ""
    sufixos = []
    while i <= len(palavra):
        sufixo = str(palavra[-i]) + str(sufixo)
        sufixos.append(sufixo)
        i += 1
    return sufixos

print(lista_sufixos('banana'))