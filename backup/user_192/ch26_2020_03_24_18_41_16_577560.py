valor = int(input('valor: '))
salario = int(input('salario: '))
anos = int(input('anos: '))

m = anos*12
p = valor/m

if p > s*0.3:
    print('Emprésrimo não aprovado')
else:
    print('Empréstimo aprovado')