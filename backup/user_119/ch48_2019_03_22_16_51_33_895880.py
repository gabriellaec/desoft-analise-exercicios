mes=input('Digite o numero do mes: ')
meses=['janeiro','fevereiro','marco','abril','maio','junho','julho','agosto','agosto','setembro','outubro','nobembro','dezembro']
c=0
while meses[c]!=mes and c<12:
    c+=1
if c>12:
    print('mês invalido')
else:
    print(c+1)

