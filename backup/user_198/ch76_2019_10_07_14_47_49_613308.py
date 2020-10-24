def aniversariantes_de_setembro(niver):
    set={}
    for nome in niver:
        if niver[nome][4]==9:
            set[nome]=niver[nome]
    return set
            