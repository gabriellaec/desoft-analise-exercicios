def faixa_notas(l1):
    lista = []
    a = 0 
    b = 0 
    c = 0
    for i in l1:
        if i < 5:
            a +=1
        if 5 <= i and i <= 7:
            b += 1
        if i >= 7:
            c += 1
    lista.append(a)
    lista.append(b)
    lista.append(c)
    return lista 
     