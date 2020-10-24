def junta_nome_sobrenome(x,y):
    nome_sobrenome = []
    for i in range(len(x)):
        nome_completo = '{0} {1}'.format(x[i],y[i])
        nome_sobrenome.append(nome_completo)
    return nome_sobrenome
