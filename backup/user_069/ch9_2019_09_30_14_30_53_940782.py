def lista_sufixos (string):
    sufixos = [] 
    i = len(string) - 1 
    sufixo = ''
    while i >= 0: 
        sufixo = string[i] + sufixo
        sufixos.append(sufixo)
        i -= 1
    return sufixos 