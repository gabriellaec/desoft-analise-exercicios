def login_disponivel (n, l):
    c = 0
    num = 0
    for i in l:
        if n != i:
            c +=1
        elif n == i:
            num += 1
            n = n + str(num)
        elif n == i and num >= 1:
            num += 1
            n = n.replace(str(num-1), str(num))
        
    if c == len(l):
        return n
    else:
        return n