def estritamente_crescente(x):
    lista = []
    c = 0 
    s = 0 
    while c < len(x):
        if s < x[c] or len(lista)==0:
            lista.append(x[c])
            s = x[c]
            print(lista)
        c +=1   
    return lista