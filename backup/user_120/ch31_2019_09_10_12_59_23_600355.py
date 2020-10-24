valor_casa = float(input('insira o valor da casa:'))
anos_pag=int(input('insira a qtd de anos para pagamento: '))
salario=float(input('insira seu salario: '))

prest= valor_casa/anos_pag/12

if prest>salario*0.3:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado')