def conta_a(x):
    a = []
    palavra = list(str(x))
    i = 1
    while i<len(palavra):
        if palavra[i]=='a':
            a.append(palavra[i])
        a += 1
    else:
        return a