def calcula_total_da_nota(a,b):
    c = []
    s = 0   
    for i in range(len(a)):
        for e in range(len(b)):
            if i == e:
                valor= a[i]*b[e]
                c.append(valor)
    for k in range(len(c)):
        s += c[k]
        
    return s