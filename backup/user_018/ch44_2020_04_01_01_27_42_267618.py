lista = ['','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
i = 0 
a = int(input('Mês = '))
for i in range(len(lista)):
    if i == a:
        print(i)