def junta_nome_sobrenome(a, b):
    i = len(a)/2
    j=0
    y = []
    while i < len(a):
        z = a[j] + ' ' + b[i]
        y.append(z)
        j = j + 1
        i = i + 1
    return y
        
        