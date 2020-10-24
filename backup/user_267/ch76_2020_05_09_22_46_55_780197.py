def aniversariantes_de_setembro(dicio_nomes_birth):
    new = dict()
    for n,i in dicio_nomes_birth.values():
        if i[n] == 'dd/{0}/aaaa'.format('09'):
            new[n] = i
    return new
            
        