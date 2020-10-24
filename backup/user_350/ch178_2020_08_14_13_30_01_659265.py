def junta_nomes(a,b,c):
    resultado = []
    for i in c:
        for n in a:
            if n != '' and i != '':
                nome_sobrenome = n + ' ' + i
                resultado.append(nome_sobrenome)
        for n in b:
            if n != '' and i != '':
                nome_sobrenome = n + ' ' + i                
                resultado.append(nome_sobrenome)
                
    return resultado