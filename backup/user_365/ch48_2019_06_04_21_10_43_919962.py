lista=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
mes=input("nome do mes")

i=0
while i<=13:
    if lista[i]==mes:
        i+=1
        print(i)
    else:
        i+=1