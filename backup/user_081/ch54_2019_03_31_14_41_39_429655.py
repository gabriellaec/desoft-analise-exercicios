def junta_nome_sobrenome(x,y):
    i = 0 
    while i < len(x):
        nome_sobrenome= x[i] + ' ' + y[i]
        print('Nome completo: ', nome_sobrenome)
        i = i + 1