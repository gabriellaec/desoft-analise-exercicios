def apaga_repetidos(s_):
    s = s_.lower()
    l = []
    t = 0
    for i in s:
        if i not in l:
            l.append(i)
        else:
            s[t] = '*'
        t+=1
    return s