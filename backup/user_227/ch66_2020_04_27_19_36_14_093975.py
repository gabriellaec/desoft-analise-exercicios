def lista_sufixos(string):
    sufixos=[]
    i=0
    while i<len(string):
        sufixo=string[i:]
        sufixos.append(sufixo)
        i+=1
    return sufixos