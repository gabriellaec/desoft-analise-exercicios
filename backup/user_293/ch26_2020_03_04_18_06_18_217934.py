valor_casa = int(input("Qual o valor da casa: "))
salario = int(input("Qual o valor do salario: "))
anos_pagar = int(input("Em quantos anos vai pagar: "))

anos_meses = anos_pagar*12
valor_prestacao = valor_casa/anos_meses

if valor_prestacao > salario*0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')

