def aniversariantes_de_setembro(dicio_nomes_birth):
    new = dict()
    for n,i in dicio_nomes_birth.items():
        if i[3:5] == '09':
            new[n] = i
    return new
            
        