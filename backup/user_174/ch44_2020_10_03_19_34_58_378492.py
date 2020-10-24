lista=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
x=(input("Que nome do mês?"))
i=0
while i<12:
    if x==lista[i]:
        print(i+1)
    i+=1
    