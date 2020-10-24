casa=int(input('Digite o valor da casa: '))
salario=int(input('Digite seu salario: ')) 
anos=int(input('Em quantos anos pretende quitar a casa ?: '))
if casa/(anos*12)>=0.3*salario:
    print ('Empréstimo não aprovado')
else:
    print ('Empréstimo aprovado') 