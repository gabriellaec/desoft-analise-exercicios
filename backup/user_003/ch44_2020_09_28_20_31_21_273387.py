lista=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
i=0
perg = input("Qual o nome?")
while i<12:
    if lista[i]==perg:
        print(i+1)
        break
    else:
        i=i+1
