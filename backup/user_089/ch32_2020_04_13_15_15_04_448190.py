def lista_primos(g):
    lista = []
    i = 3
    if g == 3:
        a = [2]
        return a
    if g == 2:
        b = []
        return []
   
        if i % 2 == 0 and i != 2 or i == 0 or i == 1:
            i = i +2 
        while i < g:
            if x % i == 0:
                i = i + 2
            else:
                lista.append(i)
        i += 2
    return lista