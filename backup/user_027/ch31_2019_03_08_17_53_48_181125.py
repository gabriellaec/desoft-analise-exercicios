valor = float(input())
sal = float(input())
anos = float(input())
parcela = (valor/(12*anos))
if (parcela/sal) > 0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')