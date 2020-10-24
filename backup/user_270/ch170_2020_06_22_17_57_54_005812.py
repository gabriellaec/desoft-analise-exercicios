def apaga_repetidos(s_):
    s = s_.lower()
    l = []
    ls = []
    t = 0
    for i in s:
        if i not in l:
            l.append(i)
            ls.append(i)
        else:
            ls.append('*')
        t+=1
    return ''.join(ls)