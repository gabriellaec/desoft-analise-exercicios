def acha_bigramas(s):
    i = 1
    l = []
    while i < len(s):
        b = s[i] + s[i-1]
        if b not in l:
            l.append(b)
        i += 1