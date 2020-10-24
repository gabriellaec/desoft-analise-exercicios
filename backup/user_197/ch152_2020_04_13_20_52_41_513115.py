def verifica_preco(tl,dl,tc):
    if tl in dl:
        cl=dl[tl]
        if cl in tc.keys():
            valor=dl[cl]
        return valor
        
        
