casa = int(input("Qual o valor da casa:?"))
salario = int(input("Qual o salario?:"))
anos = int(input("Quantos anos?:"))

prestacao = casa / (anos * 12)
if prestacao > (salario * 0.3):
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')