mes= ['início','janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
numero= ['início',1,2,3,4,5,6,7,8,9,10,11,12]
nome= input('Qual o nome do mês? ')
x= True
indice=0
while x:
    if nome == mes[indice]:
        print(numero[indice])
        x = False
    else:
        indice += 1