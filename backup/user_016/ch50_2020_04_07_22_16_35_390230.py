def junta_nome_sobrenome(nome, sobrenome):
    i = 0
    lista = []
    while i < len(nome):
        lista.append('{0} {1}'.format(nome[i], sobrenome[i]))
        i +=1
    print(lista)