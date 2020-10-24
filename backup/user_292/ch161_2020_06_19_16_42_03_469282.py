def PiWallis(n): 
    if n == 0:
        x = 0 
    else:
        a = [0,2]
        b = [0,1]
        i = 0
        while i < n:
            if i % 2 == 0:
                p = a[i] + 2
                a.append(p)
            else: 
                w = b[i] + 2
                b.append(w)
            i +=1
    A = 1
    for i in a:
        if i > 0:
            A = A * i
    B = 1
    for i in b:
        if i > 0:
            B = B * i
    
    X = A/B
    return X