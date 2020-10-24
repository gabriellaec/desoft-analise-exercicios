meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
n=input("qual o nome do mês?")
for i in meses:
    if mese[i]==n:
        numero=meses.index(n)+1
        print(numero)
        