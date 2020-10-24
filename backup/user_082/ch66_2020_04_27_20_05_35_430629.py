def lista_sufixos(string):
    sufixo=[]
    for i in range(len(string)):
        palavra= string[0:] - string[0::i]
        sufixo.append(palavra)
    return sufixo
        