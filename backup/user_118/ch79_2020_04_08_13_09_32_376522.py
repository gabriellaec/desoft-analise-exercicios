def monta_dicionario(telefone):
    agenda = {"Fulano": "99999-1111", "Sicrano": "99999-2222"}
    if telefone in agenda:
        print('O telefone de {0} é {1}'.format (agenda,telefone)
    else:
        print('O telefone de {0} não existe!'.format (agenda)