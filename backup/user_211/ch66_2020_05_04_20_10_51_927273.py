def lista_sufixos(palavra):
    sufixos=[]
    for i in palavra:
        sufixos.append(palavra[i:])
    return sufixos
    
    