def verifica_preco(tl,dl,tc):
    for tl in dl.keys():
        if dl.values(tl) in tc:
            return tc.keys(dl.values(tl))