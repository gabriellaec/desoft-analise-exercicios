n = int(input('Digite sua idade: '))


def imprime_faixa (n):
    if n < 18:
        print('jovem')
    elif n>=18 and n <60:
        print('adulto')
    elif n> 60:
        print('idoso')
    else:
        print('invalido')
        
imprime_faixa(n)