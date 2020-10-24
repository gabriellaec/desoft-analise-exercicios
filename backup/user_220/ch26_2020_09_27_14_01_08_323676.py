valor=float(input("Qual p valor da casa? "))
salario=float(input("Qual o seu salario? "))
anos=int(input("Quantos anos a pagar? "))
def meses(anos):
    meses=anos*12
    return meses
meses=meses(anos)
def prestaçao(valor,meses):
    prestaçao=valor/meses
    return prestaçao
if prestaçao<30/100*salario:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")