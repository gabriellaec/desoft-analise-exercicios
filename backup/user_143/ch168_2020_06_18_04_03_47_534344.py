def login_disponivel (n, l):
    c = 0
    for i in l:
        if n != i:
            c +=1
        elif n == i:
            n = n + '1'
        
    if c == len(l):
        return n
    else:
        return n