
mes = input('Qual o mês? ')
lista = [Janeiro,Fevereiro,Março,Abril,Maio,Junho,Julho,Agosto,Setembro,Outubro,Novembro,Dezembro]
x=0
while x<=12:
    lista[x]=x+1
    x+=1
print(lista[mes])