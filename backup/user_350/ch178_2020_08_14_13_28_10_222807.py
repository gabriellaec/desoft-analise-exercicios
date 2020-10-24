def junta_nomes(a,b,c):
    resultado = []
    for i in c:
        for nome in a:
            if nome != '' and i != '':
                nome_sobrenome = nome + ' ' + i
                resultado.append(nome_sobrenome)
        for nome in b:
            if nome != '' and i != '':
                nome_sobrenome = nome + ' ' + i                
                resultado.append(nome_sobrenome)
                
    return resultado