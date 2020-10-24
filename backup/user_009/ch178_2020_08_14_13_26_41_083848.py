def junta_nomes(l1,l2,l3):
    resultado = []
    for i in l3:
        for nome in l1:
            if nome != '' and i != '':
                nome_sobrenome = nome + ' ' + i
                resultado.append(nome_sobrenome)
        for nome in l2:
            if nome != '' and i != '':
                nome_sobrenome = nome + ' ' + i                
                resultado.append(nome_sobrenome)
                
    return resultado