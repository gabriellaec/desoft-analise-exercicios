def conta_bigramas(string):
    bigramas={}
    c=0
    while c+1<len(string):
        bigramaI=string[c:(c+2)]
        if bigramaI in bigramas:
            bigramas[bigramaI]+= 1
        else:
            bigramas[bigramaI]=1
        c+=1
    return bigramas