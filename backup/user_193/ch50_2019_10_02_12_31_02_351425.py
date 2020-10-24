def numero_no_indice(ln):
    i=0
    while i<len(ln):
        if ln[i]!=i:
            ln.remove(i)
        i+=1