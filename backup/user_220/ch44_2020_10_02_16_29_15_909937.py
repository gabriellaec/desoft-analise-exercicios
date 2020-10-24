pergunta = input("Qual o noem do mês? ")
mes = ['nenhum','janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
t=1
while t < len(mes):
    if pergunta == mes[t]:
        print(t)
    else:
        t+=1