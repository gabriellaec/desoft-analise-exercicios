nome=input("Qual o nome do mês?")
meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
ind = -1
i = 0

while i < len(meses):
    if meses[i]==nome:
        ind = i
    i+=1
    print(i)
