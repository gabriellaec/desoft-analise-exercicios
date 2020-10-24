def junta_nomes(h,m,s):
    nomes = h+m
    sob = s
    comb = []
    for n in nomes:
        for i in sob:
            comb.apend(n+''+i)
    return comb
        