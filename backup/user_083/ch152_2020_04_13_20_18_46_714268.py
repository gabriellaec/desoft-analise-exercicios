def verifica_preco(nome,dc,dl):
    if nome in dl:
        c=dl[nome]
    if c in dc:
        p=dc[c]
        return p