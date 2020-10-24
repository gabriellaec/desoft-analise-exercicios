def lista_sufixos(palavra):
    i=0
    sufixo = []
    while i<len(palavra):
        sufixo.append(palavra[i:(len(palavra))])
        i+=1
        return sufixo