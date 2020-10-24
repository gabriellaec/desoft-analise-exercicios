def lista_sufixos(string):
    sufixos=[]
    for i in len(string):
        if string[i]!= " ":
            sufixos.append(string[i])
    return sufixos