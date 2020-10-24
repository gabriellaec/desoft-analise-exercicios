lista=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
pergunta = input("Qual o nome?")
i=0
while i < 12:
    if lista[i] == pergunta:
        print(i+1)
        break
    i=i+1