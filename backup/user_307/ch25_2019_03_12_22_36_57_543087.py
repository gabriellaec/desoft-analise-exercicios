#Escreva um programa que pergunta a distância que um passageiro deseja percorrer em km. 
#Seu programa deve imprimir o preço da passagem, 
#cobrando R$0.50 por km para viagens de até 200km e R$0.45 por quilômetro extra para viagens mais longas. 
#(Adaptado do ex. 4.6 livro Nilo Ney).
#O resultado deve ser impresso com exatamente duas casas decimais.

dist=float(input('Qual distância desejada?'))

if dist<=200:
	y=dist*0.5
	print(y)
else:
	y=100+(dist*0.45)
	print(y)