def faixa_notas(n):
    i = 0
    b = 0
    m = 0
    a = 0
    while i < len(n):
        if n[i] < 5:
            b = b+1
        if n[i] >= 5 or n[i] <= 7:
            m = m+1
        if n[i] > 7 and n[i] < 11:
            a = a+1
        i=i+1
    l=[b,m,a]
    return l