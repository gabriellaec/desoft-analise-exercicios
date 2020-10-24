mes= input('qual é o nome do mes?')
nome=['janeiro','fevereiro', 'março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
i=0
while i<=len(nome):
    if mes==nome[i]:
        return x=i+1
    i+=1
print(x)

    