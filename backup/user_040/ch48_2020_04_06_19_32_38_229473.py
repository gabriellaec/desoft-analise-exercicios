def estritamente_crescente(x):
    lista = []
    if len(x) > 0:
        lista.append(x[0])
        y = 1
        s = 0
        while y < len(x):
            if x[y] > lista[s]:
                lista.append(x[y])
                y += 1
                s += 1
            else:
                y +=1
        return lista
    else:
        return []

def eh_crescente(a):
    estritamente_crescente(a)
    if a == estritamente_crescente(a):
        return True
    else:
        return False