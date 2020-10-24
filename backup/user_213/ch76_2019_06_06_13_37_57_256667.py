def aniversariantes_de_setembro(aniversario):
    dados={}
    for pessoa,data in aniversario.items():
        dia, mes, ano = data.split('/')
        if mes == '09':
            dados[pessoa] = data
    return dados
        