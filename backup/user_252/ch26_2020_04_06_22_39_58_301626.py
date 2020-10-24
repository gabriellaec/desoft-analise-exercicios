casa=float(input('valor da casa: '))
salario=float(input('salario: '))
anos=int(input('quantos anos: '))
meses=anos*12
p=casa/meses 
if p > salario*0.30:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
    