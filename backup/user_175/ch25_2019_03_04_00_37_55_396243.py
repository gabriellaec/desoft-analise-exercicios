def calcula_valor(distancia):
    if distancia <= 200:
        valor = distancia*(0.50)
    else:
        valor = 200*(0.50) + ((distancia - 200)*(0.45))
    return valor

print('---------------------------------------------------------------------')
print('Qual é a distância, em quilômetros, que o senhor(a) deseja percorrer?')
a = float(input())

print('---------------------------------------------------------------------')
print('Preço da passagem: R${:.2f}' .format(calcula_valor(a)))