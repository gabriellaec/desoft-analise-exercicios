def apaga_repetidos(s_):
    s = s_.lower()
    l = []
    for i in s:
        if i not in l:
            l.append(i)
        else:
            i = '*'
    return s