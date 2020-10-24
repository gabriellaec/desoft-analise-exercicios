def aniversariantes_de_setembro(x):
    dicioniversetembro = dict()
    for nome in x:
        data = x[nome]
        mes = data[3:5]
        if mes == '09':
            dicioniversetembro[nome] = data 
        
    print(dicioniversetembro)