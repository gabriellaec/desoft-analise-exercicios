def estritamente_crescente(x):
    lista = []
    count = 0
    s = 0
    while count<len(x):
        if s < x[count] or len(lista)==0:
            lista.append(x[count])
            s = x[count]
            print (lista)
        count +=1
    return lista