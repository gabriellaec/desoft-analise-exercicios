def retorna_soma(elementos):
    s=0
    i=0
    while i<len(elementos):
        s+=elementos[i]
        i+=1
    return s
print (retorna_soma(elementos))