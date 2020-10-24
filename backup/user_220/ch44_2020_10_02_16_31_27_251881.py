pergunta = input("Qual o nome do mês? ")
mes = ['nenhum','janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
j = True
t=1
while t < len(mes) and j:
    if pergunta == mes[t]:
        print(t)
        j = False
    else:
        t+=1