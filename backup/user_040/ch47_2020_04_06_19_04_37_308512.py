def estritamente_crescente(x):
    lista = []
    if len(x)>0:
        for e in x:
            y = 0
            if e > lista[y]:
                lista.append(e)
                y += 1
            else:
                y +=1