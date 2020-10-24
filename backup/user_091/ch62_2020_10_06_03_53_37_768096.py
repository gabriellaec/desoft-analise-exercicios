def pos_arroba(nome):
    x=0
    for x,i in nome:
        if x=='@':
            x+=1
            return '[%d]' % (x)