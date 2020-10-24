vl_casa = input(int("qual o valor da casa?"))
salario = input(int("Qual o seu salario?"))
qte_anos = input(int("em quantos anos voce quer pagar"))
qte_meses = qte_anos*12
prestacao = vl_casa/qte_meses
pct = salario*0.3
if prestacao <= pct:
    print("Empréstimo aprovado")
else:
    print("Empréstimo não aprovado")
    
                