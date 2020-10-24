mes = input('Qual o mês? ')
lista = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
x=0
while lista[x] != mes:
    x+=1
lista[x]=x+1
print(lista[x])