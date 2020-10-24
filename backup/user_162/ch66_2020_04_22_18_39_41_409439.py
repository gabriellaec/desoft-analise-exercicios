def lista_sufixos(string):
    lsufixo = []
    for i in range(len(string)):
        lsufixo.append(string[i:])
        
    return lsufixo