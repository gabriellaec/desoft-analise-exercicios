vl_casa = int(input("Qual o valor da casa?"))
salario = int(input("Qual o seu salario?"))
qte_anos = int(input("Em quantos anos voce quer pagar?"))
qte_meses = qte_anos * 12
prestacao = (vl_casa / qte_meses)
pct = (float(salario * 0.3))
if prestacao <= pct:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")

