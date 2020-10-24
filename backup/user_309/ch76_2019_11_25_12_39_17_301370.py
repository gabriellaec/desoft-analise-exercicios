def aniversariantes_de_setembro(dicio):
    new_dict = dict()
    for k,v in dicio.items():
        if v[3:5] == '09':
            new_dict[k] = v
    return new_dict