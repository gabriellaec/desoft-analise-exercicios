def aniversariantes_de_setembro(dict1):
    novo={}
    for nome,nascimento in dict1.items():
        if nascimento[4]== "9":
            novo[nome] = nascimento
    return novo
    
    
                                