def numero_no_indice(ln):
    i=0
    c=0
    while c<len(ln):
        if ln[i]!=i:
            ln.remove(i)
        i+=1