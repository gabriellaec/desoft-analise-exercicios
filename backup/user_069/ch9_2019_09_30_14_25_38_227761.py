def lista_sufixos (string):
    sufixos = [] 
    i = len(string) - 1 
    sufixo = ''
    while i >= 0: 
        sufixo += string[i]
        sufixos.append(sufixo)
        i -= 1
    return sufixos 