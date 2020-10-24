distância=float(input("Digite a distância a percorrer:"))
multa = distância - 200
excesso = multa * 0.45

if distância <= 200:
    passagem = 0.5 * distância
else:
    passagem = 0.5* distância + excesso
print("Preço da passagem: R$ %7.2f" % passagem)
