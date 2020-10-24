def estritamente_crescente(x):
    lista=[]
    i= 0
    s=0
    while i<len(y):
        if s<  x[i] or len(lista)==0:
            lista.append(x[i])
            s = x[i]
            print(lista)
        i = i + 1
    return lista        
    