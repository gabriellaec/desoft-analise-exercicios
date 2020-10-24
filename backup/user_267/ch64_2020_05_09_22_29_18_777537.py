def acha_bigramas(s):
    todos_bi = []
    i = 0
    while i <= len(s):
        todos_bi.append("{0}".format(s[i]+s[i+1]))
        i += 1
    return todos_bi
    