def numero_no_indice(ln):
    i=0
    j=[]
    while i<len(ln):
        if ln[i]==i:
            j.append(i)
        i+=1
    return j