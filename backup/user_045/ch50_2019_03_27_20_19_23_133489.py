def numero_no_indice(n):
    while i<len(n):
        if n[i]!=i:
            del n[i]
        i+=1
    return n
            