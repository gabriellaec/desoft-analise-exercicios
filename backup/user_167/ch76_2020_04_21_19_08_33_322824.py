def aniversariantes_de_setembro (dic):
    nv={}
    for k,v in dic. items():
        if v[4]=="9":
            nv[k]=v
    return nv