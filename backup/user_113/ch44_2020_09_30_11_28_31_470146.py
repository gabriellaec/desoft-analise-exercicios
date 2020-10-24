mes = input('Qual o mês? ')
lista = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

x=True
i=0
while x==True:
    if mes == lista[i]:
        lista[i]= i+1
        x = False
    else:
        i+=1
print(i)