def pos_arroba(string):
    i=0
    c=0
    while i < len(string):
        if string[i] =="@":
            c=i
        i=i+1
    return c