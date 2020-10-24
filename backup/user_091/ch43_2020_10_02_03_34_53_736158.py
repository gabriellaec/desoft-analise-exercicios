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
meses=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
numeros=[1]
i=0
while i<11:
    numeros.append(numeros[i]+1)
    i+=1
x=int(input('Digite o número mês desejado: '))
print(meses[x-1])
    


    