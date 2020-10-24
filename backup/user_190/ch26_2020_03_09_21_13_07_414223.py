valor=int(input('qunato custa a casa?: '))
salario=int(input('qual seu salário?: '))
anos=int(input('quantos anos vc ira pagar?: '))
prestação=valor/(anos*12)
if (prestação>salario*0.3):
    print ('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')