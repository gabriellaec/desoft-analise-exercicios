def verifica_preco(stri_ndl, tab_ct, tab_cp):
    cor = 'cor'
    preco = 0
    for t, c in tab_ct.items():
        if t == stri_ndl:
            cor = c
    for co, pre in tab_cp.items():
        if cor == co:
            preco = pre
    return preco