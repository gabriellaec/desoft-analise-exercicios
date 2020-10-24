def junta_nomes(h,m,s):
    nomes = h+m
    sob = s
    comb = []
    for n in nomes:
        for i in sob:
            comb.append(n+''+i)
    return comb
        