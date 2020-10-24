def lista_sufixos(string):
    sufixo=[]
    for i in range(len(string)):
        palavra= string[:] - string[::i]
        sufixo.append(palavra)
    return sufixo
        