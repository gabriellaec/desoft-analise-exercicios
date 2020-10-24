def aniversariantes_de_setembro(nome_e_data):
    aniversariantes={}
    for a in nome_e_data:
        if nome_e_data[a[3]]=='0' and nome_e_data[a[4]]=='9':
            aniversariantes[a]=nome_e_data[a]
    return aniversariantes