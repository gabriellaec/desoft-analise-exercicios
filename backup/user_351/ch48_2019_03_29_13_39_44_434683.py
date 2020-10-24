meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
mes = input("qual o mês?")
c = 0
while meses[c] != mes and c<12:
    c+=1
print (c + 1)