pergunta=input('fala um mes')
lista=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
i=1
while lista[i-1]!=pergunta:
    i+=1
print(i)