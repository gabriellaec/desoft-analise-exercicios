def login_disponivel (n, l):
    c = 0
    num = 0
    for i in l:
        if n != i:
            c +=1
        elif n == i:
            num += 1
            n = n + str(num)
        
    if c == len(l):
        return n
    else:
        return n