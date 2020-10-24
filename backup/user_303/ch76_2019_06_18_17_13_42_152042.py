def aniversariantes_de_setembro(dados):
    aniversariantes={}
    for nome in dados:
        if dados[nome][3] == '0' and dados[nome][4] == '7':
            aniversariantes[nome]=dados[nome]
    return aniversariantes 