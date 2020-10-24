def aniversariantes_de_setembro(aniversario):
    dados={}
    for pessoa,data in aniversario.items():
        if data[3:5]=='09':
            dados[pessoa]=data
    return dados
        