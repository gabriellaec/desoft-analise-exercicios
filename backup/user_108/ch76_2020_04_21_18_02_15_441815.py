def aniversariantes_de_setembro(aniversarios):
    return {nome:data for nome,data in aniversarios.items() if nome[3:5] == "09"} 