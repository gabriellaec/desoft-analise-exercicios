nome= str(input("escreva o nome de um mês: "))
lista_nomes=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
contador = 0
while contador < len(lista_nomes):
    if nome != lista_nomes[contador]:
    	contador +=1
numero_mes= contador+1
print(numero_mes)