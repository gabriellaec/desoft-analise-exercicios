#definindo a distância
distância = float(input('Quanto deseja percorrer em km: '))
#determinando preço da passagem
if distância <= 200:
    preço_passagem = distância*0.5
elif distância > 200:
    preço_passagem = 100 + (distância-200)*0.45
#imprimindo o preço da passagem
print('O preço da passagem é {0:.2f}'.format(preço_passagem))