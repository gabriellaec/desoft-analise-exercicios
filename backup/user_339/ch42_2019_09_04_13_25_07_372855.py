def quantos_uns(n):
    s = 0
    i = 0
    x = list(str(n))
    l = len(x)
    while i < l:
        if '1' in x[i]:
            s += 1
        i += 1
    print(s)
       
 