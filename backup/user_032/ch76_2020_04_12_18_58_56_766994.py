def aniversariantes_setembro(nome):
    set = {}
    data = nome.values()
    i=0
    for k,v in nome.items():
        if v[3]=='0' and v[4]=="9":
            set[k]=v
            i+=1
    return set