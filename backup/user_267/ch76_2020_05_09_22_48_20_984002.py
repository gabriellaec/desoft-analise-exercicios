def aniversariantes_de_setembro(dicio_nomes_birth):
    new = dict()
    for i in dicio_nomes_birth.items():
        if i == 'dd/{0}/aaaa'.format('09'):
            new = i         
    return new
            
        