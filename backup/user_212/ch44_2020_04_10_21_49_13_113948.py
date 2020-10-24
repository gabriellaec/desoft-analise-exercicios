mes_numero={'Janeiro':1, 'Fevereiro':2, 'Março': 3, 'Abril':4, 'Maio':5, 'Junho':6, 'Julho':7, 'Agosto':8, 'Semtembro':9, 'Outubro':10, 'Novembro':11, 'Dezembro':12}

mes=input('Escolha um mês')

if mes in mes_numero:
    N=mes_numero
    print ('Mês {0}'.format(N))