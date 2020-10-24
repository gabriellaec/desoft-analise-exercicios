def lista_sufixo(string):
    sufixo=[]
    for i in range(len(string)):
        sufixo.append(string)
        string-=string[i]
    return sufixo