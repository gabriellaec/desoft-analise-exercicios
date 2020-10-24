def junta_nome_sobrenome(a, b):
    i = len(a)/2
    j=0
    y = []
    while i < len(a):
        y.append(a[j] + ' ' + b[i])
        j = j + 1
        i = i + 1
    return y
        
        