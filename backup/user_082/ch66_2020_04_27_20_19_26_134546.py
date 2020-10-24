def lista_sufixos(string):
    sufixo=[]
    for i in range(len(string)):
        sufixo.append(string[i:])
    return sufixo
   

        