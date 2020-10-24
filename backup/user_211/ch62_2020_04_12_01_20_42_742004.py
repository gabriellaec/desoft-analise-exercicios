def pos_arroba(string):
    n=0
    for i in string:
        if i=='@':
            n=string.index(i)
    return n