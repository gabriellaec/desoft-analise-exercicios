def lista_sufixos(string):
    suf=string
    listasuf=[]
    while suf!=[]:
        listasuf.append(suf)
        suf=suf[1:]
    return listasuf