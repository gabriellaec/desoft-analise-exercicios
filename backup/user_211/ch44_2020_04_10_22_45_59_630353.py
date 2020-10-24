meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
n=input("qual o nome do mês?")
for i in range(0,len(meses)):
    if meses[i]==n:
        print(meses.index[i]+1)
        