def verifica_preco(tl, dl, tc):
    if tl in dl:
        c = dl[tl]
        if c in tc:
            p = tc[c]
            return p