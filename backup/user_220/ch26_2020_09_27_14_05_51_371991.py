valor=int(input("Qual o valor da casa? "))
salario=int(input("Qual o seu salario? "))
anos=int(input("Quantos anos a pagar? "))
def meses(anos):
    meses=anos*12
    return meses
meses=meses(anos)
def prestaçao(valor,meses):
    prestaçao=valor/meses
    return prestaçao
prestaçao=prestaçao(valor,meses)
def x(salario):
    x=salario*30/100
    return x
x=x(salario)
if prestaçao>x:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")