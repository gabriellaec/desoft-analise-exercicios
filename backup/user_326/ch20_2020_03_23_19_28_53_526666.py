d = int(input('Qual a distância que vai percorrer (em Km)? '))

if d <= 200:
    preço1 = d * 0.50
    print ('O valor de sua passagem é: R${0:.2f}'.format(preço1))
else:
    valor1 = 200 * 0.5
    valor2 = (d - 200) * 0.45
    preço2 = valor1 + valor2
    print ('O valor de sua passagem é: R${0:.2f}'.format(preço2))
    