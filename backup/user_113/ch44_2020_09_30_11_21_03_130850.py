mes = input('Qual o mês? ')
lista = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
x=0
while lista[x] != mes and x<12:
    print(x)
    x+=1
x+=1
print(x)