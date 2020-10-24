distância = float(input("Digite a distância a percorrer: "))
if distância <= 200:
    passagem = 0.5 * distância
else:
    passagem = 0.45 * distância
print("o preco da passagem é R${0:.2f}".format(passagem))