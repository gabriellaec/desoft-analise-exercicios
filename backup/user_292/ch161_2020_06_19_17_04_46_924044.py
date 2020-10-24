def PiWallis(n): 
    if n == 0:
        X = 0 
    if n == 1 :
        X = 4
    else:
        a = [0,2,2]
        b = [0,1,3]
        i = 2
        while i < n:
            if i % 2 == 0:
                p = a[i] + 2
                a.append(p)
                b.append(b[i])
            else: 
                w = b[i] + 2
                b.append(w)
                a.append(a[i])
            i +=1
        A = 1
        for i in a:
            if i > 0:
                A = A * i
        B = 1
        for i in b:
            if i > 0:
                B = B * i
                
        X = 2 * A/B
    return X