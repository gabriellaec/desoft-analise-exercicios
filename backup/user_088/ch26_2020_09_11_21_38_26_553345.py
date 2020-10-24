valor = float(input("Digite o valor da casa: "))
salário = float(input("Digite o salário: "))
anos = int(input("Quantos anos para pagar: "))
meses=12*anos
prestacao=valor/meses
if(prestacao>0.3*salário):
    print ('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')