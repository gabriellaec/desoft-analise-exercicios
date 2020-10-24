def lista_sufixos(string):
    suf=string
    listasuf=[]
    while suf!='':
        suf=suf[:-1]
        listasuf.append(suf)
    return listasuf