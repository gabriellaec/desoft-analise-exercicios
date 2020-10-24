mes = input('Qual o mês? ')
lista = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
x=0
while mes != lista[x]:
    lista[x] = x+1
    x+=1
print(lista[x])