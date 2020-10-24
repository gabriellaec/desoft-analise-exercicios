def conta_bigramas(string):
    vazio={}
    f=0
    for f in renge len(string)-1 :
        key= string[f]+string[f+1]
        if key not in vazio:
            vazio[key]=1
        else:
            vazio[key]+=1
        return vazio