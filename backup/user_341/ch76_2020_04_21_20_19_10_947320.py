def aniversariantes_de_setembro(aniversarios):
    anive_setembro = {}
    for i in aniversarios:
        if aniversarios[i][4] == "9":
            anive_setembro[i] = aniversarios[i]
    return anive_setembro