strmes=input('qual o nome do mês escolhido? ')
listastr=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
contador=0
while contador<len(listastr):
    if strmes==listastr[contador]:
        print(contador+1)
    contador+=1
