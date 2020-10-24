def lista_sufixos(palavra):
    sufixos=[]
    for i in range(0,len(palavra)):
        sufixos.append(palavra[i:])
    return sufixos
    
    