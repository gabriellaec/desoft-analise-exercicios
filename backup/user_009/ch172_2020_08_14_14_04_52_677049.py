def imprime_faixa(numero):
    if numero < 18:
        print('jovem')
    elif numero >= 18 and numero < 60:
        print('adulto')
    elif numero >=60:
        print('idoso')