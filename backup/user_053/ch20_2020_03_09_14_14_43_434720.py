def preco_da_passagem(distancia,bagagem):
    y=0.50*distancia+0.45*bagagem
    return y

a=float(input('Distância em km: '))
b=float(input('Peso da bagagem em kg: '))
c=preco_da_passagem(a,b)

print('O preço total é de R$ {0:.2f}'.format(c))