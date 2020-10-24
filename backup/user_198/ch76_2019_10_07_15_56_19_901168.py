def aniversariantes_de_setembro(niver):
    september={}
    for nome in niver:
        if niver[nome][4]=='9':
            september[nome]=niver[nome]
    return september
            