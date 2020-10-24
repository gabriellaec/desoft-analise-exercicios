mes=int(input('n do mes'))
meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
i=0
while i<len(meses):
    if mes-1==i:
        print(meses[i])
    i+=1