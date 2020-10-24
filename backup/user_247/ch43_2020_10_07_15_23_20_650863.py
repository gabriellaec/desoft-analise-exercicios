pergunta= int(input("Escolha o número do mês"))

lista1= ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

i= 0 
while i < 12:
if pergunta == i:
    print(lista1[i+1])
