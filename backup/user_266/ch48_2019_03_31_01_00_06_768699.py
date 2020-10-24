mes=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
d=input('Qual o nome do mês? ')
n=['1','2','3','4','5','6','7','8','9','10','11','12']
i=0
while i<len(mes):
    if d==mes[i]:
        print (n[i])
    else:
        print('Este mês não existe, digite outro: ')
    i+=1    