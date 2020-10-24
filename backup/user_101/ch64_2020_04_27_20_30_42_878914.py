def acha_bigramas(s):
    i = 1
    l = []
    while i < len(s):
        b = s[i+1] + s[i]
        if b not in l:
            l.append(b)
        i += 1
    print (l)
    return l
