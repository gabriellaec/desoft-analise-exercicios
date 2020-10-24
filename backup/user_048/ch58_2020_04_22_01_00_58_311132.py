def conta_a(palavra):
    letra='a'
    i=0
    for e in range(len(palavra)):
        if palavra[e:e+len(letra)]== letra:
            i+=1
    return i