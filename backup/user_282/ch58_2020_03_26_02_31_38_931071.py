def conta_a(x):
    a = []
    palavra = list(str(x))
    i = 0
    while i<len(palavra):
        if palavra[i]=='a':
            a.append(palavra[i])
        i += 1
    else:
        return len(a)