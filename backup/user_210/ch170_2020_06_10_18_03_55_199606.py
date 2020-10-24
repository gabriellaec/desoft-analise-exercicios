def apaga_repetidos(s):
    l = []
    for each in range(len(s)):
        if s[each] not in l:
            l.append(s[each])
        else:
            s[each] = "*"
    return s