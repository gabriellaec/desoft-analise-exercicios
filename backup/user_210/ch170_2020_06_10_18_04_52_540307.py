def apaga_repetidos(s):
    l = []
    word = ""
    for each in range(len(s)):
        if s[each] not in l:
            l.append(s[each])
            word += s[each]
        else:
            word += "*"
    return word