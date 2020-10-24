valor_casa=int(input("Preço da casa? "))
salario=int(input("salário recebido? "))
parcelas=int(input("Quantos anos irá pagar? "))
def valor_parcelas(valor_casa,parcelas):
    valor_parcelas=valor_casa/(parcelas*12)
    return valor_parcelas
if valor_parcelas(valor_casa,parcelas) <= salario*0.3:
       print('Empréstimo aprovado')
else:
        print('Empréstimo não aprovado')