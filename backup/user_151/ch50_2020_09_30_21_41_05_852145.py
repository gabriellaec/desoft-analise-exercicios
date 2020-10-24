def junta_nome_sobrenome(a, b):
    j=0
    y = []
    while j < len(a):
        z = a[j] + ' ' + b[j]
        y.append(z)
        j = j + 1
    return y
        
        