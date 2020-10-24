def lista_sufixos(string):
    suf=string
    listasuf=[]
    while suf!=string[-1]:
        suf=suf[1:]
        listasuf.append(suf)
    return listasuf