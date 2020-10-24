def junta_listas(ll):
    l = ll[0]
    i = 1
    while i < len(ll):
        l += ll(i)
        i += i
    return l