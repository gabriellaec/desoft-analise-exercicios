def lista_caracteres(string):
    x=list(string)
    dic={}
    for i in x:
        dic[i]=0
    return dic.keys()