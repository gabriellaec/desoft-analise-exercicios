def aniversariantes_de_setembro(aniversariantes):
    AniSetembro = {}
    for nome in aniversariantes:
        data = nome[aniversariantes]
        if data[4] == "9":
            AniSetembro[nome] = nome[aniversariantes]
    return AniSetembro