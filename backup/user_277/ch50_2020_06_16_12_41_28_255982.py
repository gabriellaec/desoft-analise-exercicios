def junta_nome_sobrenome(nome, sobrenome):
    i = 0
    lista2 = []
    while i < len(nome):
        lista2.append('{0} {1}'.format(nome[i], sobrenome[i]))
        i+=1
    return(lista2)
        