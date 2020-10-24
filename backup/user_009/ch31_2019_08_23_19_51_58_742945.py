casa = int(input('valor casa: '))
sal = int(input('sal: '))
anos = int(input('anos: '))
if (casa / anos*12) < sal*0.3:
    print('Empréstimo aprovado')
else:
    print('Empréstimo não aprovado')