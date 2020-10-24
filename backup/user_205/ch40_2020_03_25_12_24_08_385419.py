def soma_valores(a):
    a = []
    batata = len(a)
    i = 0
    while i<len(a):
        a[i+1] = a[i] + i
    y = sum(a)
    i+=1
    return y