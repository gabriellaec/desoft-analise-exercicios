def aniversariantes_de_setembro(aniversariantes):
    AniSetembro = {}
    for nome in aniversariantes:
        data = aniversariantes[nome]
        if data[4] == "9":
            AniSetembro[nome] = aniversariantes[nome]
    return AniSetembro