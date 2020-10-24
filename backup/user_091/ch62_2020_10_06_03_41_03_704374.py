def pos_arroba(nome):
    for x in nome:
        if x=='@':
            return '{[0]}'.format(x)