def verifica_preco(tl,dl,tc):
    for tl in dl:
        if dl.values() in tc:
            return tc.keys()