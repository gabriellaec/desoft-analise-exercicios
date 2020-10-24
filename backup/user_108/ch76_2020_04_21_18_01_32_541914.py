def aniversariantes_de_setembro(aniversarios):
    return {nome:data for nome,data in aniversarios.items() if nome[4:6] == "08"} 