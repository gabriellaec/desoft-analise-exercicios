def estritamente_crescente(x):
    lista = []
    y = 0
    if len(x) > 0:
        lista.append(x[0])
        for e in x:
            número = lista[y]
            if e > número:
                lista.append(e)
                y += 1
            else:
                y +=1        
    else:
        return None
    return lista