def aniversariantes_de_setembro(aniversario):
    dados={}
    for pessoa,data in aniversario.items:
        if data[4:6]=='09':
            dados[pessoa]=data
    return dados
        