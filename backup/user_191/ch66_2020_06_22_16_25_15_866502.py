def lista_sufixos(l):
    new_str=[]
    for i in range(len(l)):
        new_str.append(l[i:])
    return new_str