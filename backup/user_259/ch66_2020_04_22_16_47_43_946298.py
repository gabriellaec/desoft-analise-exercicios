def lista_sufixos(palavra):
    i = 0
    sufixos = []
    while i<len(palavra):
        sufixos.append(palavra[i:len(palavra)])
        i+=1
    return sufixos