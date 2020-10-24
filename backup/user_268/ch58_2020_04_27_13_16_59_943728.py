def conta_a(st):
    x = 0
    a = len(st)
    for i in range(a):
        if st(i) == 'a':
            x+=1
        else:
            x = x
    return x