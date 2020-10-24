valor = float(input("Digite o valor da casa: "))
salário = float(input("Digite o salário: "))
anos = int(input("Quantos anos para pagar: "))
prestacao=valor/12*anos
if(prestacao>0.3*salario):
    print ('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')