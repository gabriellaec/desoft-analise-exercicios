def  aniversariantes_de_setembro(aniversarios):
    aniversario2 = {}
    for nome in aniversarios:
        if '/09/' in aniversarios[nome]:
            aniversario2[nome] = aniversarios[nome]
    return aniversario2
