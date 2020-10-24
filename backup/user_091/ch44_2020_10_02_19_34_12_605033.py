print('''
        MESES
------------------------
1-Janeiro
2-Fevereiro
3-Março
4-Abril
5-Maio
6-Junho
7-Julho
8-Agosto
9-Setembro
10-Outubro
11-Novembro
12-Dezembro
''')
numeros=[1,2,3,4,5,6,7,8,9,10,11,12]
meses=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
x=input('Digite o nome do mês que você deseja: ')
i=0
while i<12:
    if x== meses[i]:
        print('{0}'.format(i+1))
        i+=1
   