def junta_nome_sobrenome(a, b):
    w = len(a)
    i = int(w/2)
    j=0
    y = []
    while i < w:
        z = a[j] + ' ' + b[i]
        y.append(z)
        j = j + 1
        i = i + 1
    return y

        
        