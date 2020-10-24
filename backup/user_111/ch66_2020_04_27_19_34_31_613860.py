def lista_sufixos(palavra):
    i=0
    sufixo=[]
    while i<len(palavra):
        if i==0:
            sufixo.append(palavra)
        else:
            sufixo[i]=palavra[i:len(palavra)]
    return sufixo